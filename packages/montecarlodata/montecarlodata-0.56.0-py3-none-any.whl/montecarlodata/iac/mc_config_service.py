import contextlib
import fnmatch
import glob
import json
import os
import re
from datetime import datetime, timezone
from functools import reduce
from typing import Any, Callable, Dict, List, Optional, Set, Tuple

import click
import yaml
from box import Box
from marshmallow import ValidationError
from pycarlo.core import Client, Query
from tabulate import tabulate
from yaml import SafeLoader

from montecarlodata.config import Config
from montecarlodata.errors import complain_and_abort, manage_errors
from montecarlodata.fs_utils import mkdirs
from montecarlodata.iac.client import MonteCarloConfigTemplateClient
from montecarlodata.iac.schemas import (
    ProjectConfig,
    ResourceModification,
    ConfigTemplateUpdateState,
)
from montecarlodata.iac.utils import (
    has_montecarlo_property,
    is_dbt_schema,
    has_namespace_property,
)
from montecarlodata.settings import PROJECT_CONFIG_FILENAME, TARGET_DIRECTORY_NAME
from montecarlodata.utils import GqlWrapper


class SafeLineLoader(SafeLoader):
    def construct_mapping(self, node, deep=False):
        mapping = super(SafeLineLoader, self).construct_mapping(node, deep=deep)
        # Add 1 so line numbering starts at 1
        mapping["yaml_line"] = node.start_mark.line + 1
        mapping["yaml_file_name"] = node.start_mark.name
        return mapping


class MonteCarloConfigService:
    NS_HEADERS = ("Namespace", "Last Update Time")
    MORE_NS_MESSAGE = (
        "There are more namespaces available. Increase the limit to view them."
    )
    DBT_REF_PATTERN = re.compile(r"\[\[\s*ref\(['\"](\w+)['\"]\)\s*\]\]")
    SQL_KEYS = {"sql", "sampling_sql", "variables"}

    def __init__(
        self,
        config: Config,
        pycarlo_client: Client,
        request_wrapper: Optional[GqlWrapper] = None,
        project_dir: Optional[str] = None,
        dbt_manifest_path: Optional[str] = None,
        print_func: Optional[Callable] = None,
    ):
        request_wrapper = request_wrapper or GqlWrapper(config)
        self.client = MonteCarloConfigTemplateClient(request_wrapper)
        self._pycarlo_client = pycarlo_client
        self._print_func = print_func or click.echo
        self.project_dir = os.path.abspath(project_dir) if project_dir else os.getcwd()
        self.dbt_manifest_path = (
            os.path.abspath(dbt_manifest_path) if dbt_manifest_path else None
        )
        self._abort_on_error = True

        # Nicer formatting for multiline strings
        yaml.add_representer(str, self._str_presenter)

    def _init_local_config(self):
        self.target_dir = self._create_target_directory()
        self.project_config = self._load_project_config()

    def _init_dbt_config(self):
        self.dbt_project = self._get_dbt_project_name()
        self.dbt_nodes = self._load_dbt_manifest_nodes()

    @manage_errors
    def apply(
        self,
        apply_namespace: str,
        dry_run: bool = False,
        skip_confirmation: bool = False,
        abort_on_error=True,
    ):
        """
        Compile configuration.
        Submit configuration via API
        """
        _, ns_mc_config_dict, _ = self.compile(apply_namespace, abort_on_error)
        assert self.project_config is not None
        responses = []
        for namespace, mc_config_dict in ns_mc_config_dict.items():
            self._print_func(
                "----------------------------------------------------------------"
            )
            self._print_func(f"Computing changes for namespace: {namespace}")
            self._print_func(
                "----------------------------------------------------------------"
            )
            response = self.client.apply_config_template(
                namespace,
                mc_config_dict,
                resource=self.project_config.default_resource,
                dry_run=True,
                misconfigured_as_warning=True,
            )
            self._check_apply_errors(response, abort_on_error)

            if response.warnings:
                click.echo()
                misconfigured_warnings = response.warnings.get(
                    "misconfigured_warnings", []
                )
                if misconfigured_warnings:
                    click.echo(
                        "Warnings encountered, please review to avoid "
                        "creating misconfigured monitors:"
                    )
                    self._echo_misconfigured_warnings(misconfigured_warnings)

            if response.resource_modifications:
                self._print_func()
                self._print_func("Modifications:")
                for resource_modification in response.resource_modifications:
                    self._print_func(
                        f' - {"[DRY RUN] " if dry_run else ""}{resource_modification.type}'
                        f"\n{resource_modification.description}"
                        f"\n{self._generate_significance_text(resource_modification)}"
                    )
                self._print_func()

                if dry_run:
                    self._print_func("Dry run, none of the changes have been applied.")
                    self._print_func()
                elif skip_confirmation or click.confirm(
                    "Do you want to apply this change?", abort=False
                ):
                    response = self.client.apply_config_template(
                        namespace,
                        mc_config_dict,
                        resource=self.project_config.default_resource,
                        dry_run=False,
                        misconfigured_as_warning=True,
                    )
                    success = self._check_apply_errors(response, abort_on_error)

                    if success:
                        self._print_func("Changes successfully applied.")
                    else:
                        self._print_func("Failed to apply changes.")
                    self._print_func()
                else:
                    self._print_func("None of the changes have been applied.")
            else:
                self._print_func()
                self._print_func("No changes to configuration found, doing nothing.")
                self._print_func()
            responses.append(response)
        return responses

    def _check_apply_errors(
        self,
        response: ConfigTemplateUpdateState,
        abort_on_error: bool,
    ) -> bool:
        if response.state == "SKIPPED":
            self._print_func()
            self._print_func("Update skipped in favor of more recent update.")

            if abort_on_error:
                complain_and_abort("Update skipped, exiting.")

            return False

        if not response.errors:
            return True

        self._print_func()
        self._print_func("Errors encountered when attempting to apply configuration:")

        system_error = response.errors.get("system_error", {})
        if system_error:
            self._print_func(f" - {system_error}")
        else:
            validation_errors = response.errors.get("validation_errors", {})
            try:
                error_json = json.dumps(validation_errors, indent=2)
            except Exception as e:
                error_json = f"Couldnt parse the validation errors: {e}\nraw errors: {validation_errors}"
            self._print_func(f" - Validation error:\n{error_json}")

        self._print_func()

        if abort_on_error:
            complain_and_abort("Errors encountered, exiting.")

        return False

    @staticmethod
    def _generate_significance_text(resource_modification: ResourceModification):
        if resource_modification.is_significant_change:
            return "\n   WARNING: This is a significant change which will reset/retrain the monitor."
        return ""

    @staticmethod
    def _echo_misconfigured_warnings(misconfigured_warnings: List[Dict[str, Any]]):
        for group in misconfigured_warnings:
            click.echo(f" - {group['title']}:")
            for item in group["items"]:
                click.echo(f"     - {item}")

    @manage_errors
    def compile(
        self, apply_namespace, abort_on_error=True
    ) -> Tuple[List[str], Dict[str, Box], Dict[str, Any]]:
        """
        Gather monitor configuration YAML files from project.
        This may also include dbt schema files with meta properties
        """
        self._init_local_config()
        self._print_func()
        self._print_func("Gathering monitor configuration files.")
        assert self.project_config is not None
        files = self._gather_yaml_files(self.project_config)

        if self.project_config.namespace:
            self._print_func(
                f"namespace: {self.project_config.namespace} found in {PROJECT_CONFIG_FILENAME} ignoring value passed with --namespace={apply_namespace}"
            )
            apply_namespace = self.project_config.namespace

        if self.dbt_manifest_path:
            self._init_dbt_config()

        errors_by_file = {}
        ns_mc_config_list_map: Dict[str, List[Box]] = {}

        found_config = False

        files = sorted(list(files))
        for file in files:
            if os.stat(file).st_size == 0:
                self._print_func(f" - Skipping {file}, empty file.")
                continue
            with open(file, "r") as f:
                try:
                    yaml_as_dict = Box(yaml.load(f, Loader=SafeLineLoader))
                except Exception as e:
                    errors_by_file[file] = [f"Failed to parse YAML: {e}"]
                    self._print_func(f" - Skipping {file}, not a valid YAML file.")
                    continue
            namespace = apply_namespace
            if has_namespace_property(yaml_as_dict):
                # override apply_namespace with namespace in the yaml file.
                namespace = yaml_as_dict.namespace

            if not namespace:
                errors_by_file[file] = [
                    f"A default namespace need to be passed through command line --namespace or "
                    f"set default namespace in {PROJECT_CONFIG_FILENAME} or "
                    f"an override namespace needs to be set in file: {file}"
                ]
                continue
            if namespace not in ns_mc_config_list_map:
                ns_mc_config_list_map[namespace] = []
            mc_config_list = ns_mc_config_list_map[namespace]

            # This file is a dbt schema file.
            # Let's attempt to parse out special embedded MC sections from meta:
            # See https://docs.getdbt.com/reference/resource-properties/meta
            if is_dbt_schema(yaml_as_dict):

                # need to reload again without the yaml_line and yaml_file_name properties
                with open(file, "r") as reload_file:
                    yaml_as_dict = Box(yaml.safe_load(reload_file))

                for model in yaml_as_dict.models:
                    with contextlib.suppress(KeyError):
                        if model.meta:
                            mc_config = model.meta.montecarlo
                            errors = self._validate_mc_config(mc_config)
                            if self.dbt_manifest_path:
                                mc_config = Box(self._resolve_templates(mc_config))
                            mc_config_list.append(mc_config)
                            found_config = True
                        else:
                            errors = ["meta tag should be removed if its empty"]
                        if errors:
                            errors_by_file[file] = errors
                        self._print_func(
                            f" - {file} - Embedded monitor configuration found."
                        )

            # This file has a root montecarlo property
            # This can be in a standalone file, and also a dbt schema file
            if has_montecarlo_property(yaml_as_dict):
                mc_config = yaml_as_dict.montecarlo
                mc_config.pop("yaml_line", None)
                mc_config.pop("yaml_file_name", None)
                errors = self._validate_mc_config(mc_config)
                if self.dbt_manifest_path:
                    mc_config = Box(self._resolve_templates(mc_config))
                if errors:
                    errors_by_file[file] = errors
                mc_config_list.append(mc_config)
                found_config = True
                self._print_func(f" - {file} - Monitor configuration found.")

        # Exit if there are errors
        if errors_by_file:
            self._print_func()
            self._print_func("Configuration validation errors:")
            for file, errors in errors_by_file.items():
                self._print_func(f" - File: {file}")
                for error in errors:
                    self._print_func(f"    - {error}")
            self._print_func()
            if abort_on_error:
                complain_and_abort("Errors encountered, exiting.")

        if (not found_config) and abort_on_error:
            complain_and_abort(
                "Sorry, we didn't find any YAML files containing "
                "Monte Carlo configuration."
            )

        ns_compiled_mc_config: Dict[str, Box] = {}
        for namespace, mc_config_list in ns_mc_config_list_map.items():
            # Merge configs into a single config
            compiled_mc_config = self._merge_mc_configs(mc_config_list)

            # Write configs to target directory. Useful for debugging.
            with open(
                os.path.join(
                    self.target_dir, f"{namespace}_montecarlo_configuration.yml"
                ),
                "w",
            ) as f:
                f.write(compiled_mc_config.to_yaml())

            with open(
                os.path.join(
                    self.target_dir, f"{namespace}_montecarlo_configuration.json"
                ),
                "w",
            ) as f:
                json.dump(compiled_mc_config, f, indent=4)

            ns_compiled_mc_config[namespace] = compiled_mc_config

        return files, ns_compiled_mc_config, errors_by_file

    def _create_target_directory(self) -> str:
        target_dir = os.path.join(self.project_dir, TARGET_DIRECTORY_NAME)
        mkdirs(target_dir)
        return target_dir

    def _load_project_config(self) -> Optional[ProjectConfig]:
        contents = None
        try:
            with open(
                os.path.join(self.project_dir, PROJECT_CONFIG_FILENAME), "r"
            ) as f:
                contents = f.read()
        except FileNotFoundError:
            complain_and_abort(
                f"Not a Monte Carlo project. Must define {PROJECT_CONFIG_FILENAME} "
                "in current working directory."
            )

        assert contents is not None
        project_config_as_dict = yaml.safe_load(contents)
        try:
            s = ProjectConfig.schema()  # type: ignore
            return s.load(project_config_as_dict)
        except ValidationError as e:
            complain_and_abort(
                f"Encountered a validation problem in {PROJECT_CONFIG_FILENAME}: "
                f"{e.messages}"
            )

    def _merge_mc_configs(self, mc_config_list: List[Box]) -> Box:
        """
        Merge multiple mc configs into a single one.
        Nested dicts will be merged
        Nested lists will be concatenated
        """

        def merge_configs(x: Box, y: Box):
            # box_merge_lists="extend" does not recurse, so we need to process the
            # first config level ourselves to account for groups (like 'notifications')
            for (key, value) in y.items():
                if key in x:
                    if isinstance(value, dict):
                        x[key].merge_update(y[key], box_merge_lists="extend")
                    elif isinstance(value, list):
                        x[key].extend(y[key])
                else:
                    x[key] = value

            return x

        compiled_mc_config = reduce(merge_configs, mc_config_list)
        compiled_mc_config.pop(
            "box_merge_lists", None
        )  # Strangely enough, Box adds this add'l key. Remove it
        return compiled_mc_config

    def _validate_mc_config(self, mc_config_dict: Box) -> List[str]:
        """
        Perform simple validation.
        More comprehensive validation is performed server-side
        """
        expected_keys = [
            "field_health",
            "dimension_tracking",
            "json_schema",
            "custom_sql",
            "freshness",
            "volume",
        ]

        errors = []
        for key in expected_keys:
            with contextlib.suppress(KeyError):
                if key in mc_config_dict and not isinstance(mc_config_dict[key], list):
                    errors.append(f'"{key}" property should be a list.')
        return errors

    def _gather_yaml_files(self, project_config: ProjectConfig) -> Set[str]:
        files = set()
        for pattern in project_config.include_file_patterns:  # type: ignore
            for fn in glob.glob(
                os.path.join(self.project_dir, pattern), recursive=True
            ):
                files.add(fn)
        for pattern in project_config.exclude_file_patterns:  # type: ignore
            excluded = set(
                fnmatch.filter(files, os.path.join(self.project_dir, pattern))
            )
            files = files - excluded
        return files

    def _get_dbt_project_name(self) -> str:
        dbt_project = os.path.join(self.project_dir, "dbt_project.yml")
        try:
            with open(dbt_project, "r") as f:
                return yaml.safe_load(f)["name"]
        except Exception:
            complain_and_abort(f"Failed to read dbt project name from {dbt_project}.")

    def _load_dbt_manifest_nodes(self) -> dict:
        try:
            with open(self.dbt_manifest_path, "r") as f:
                return json.load(f)["nodes"]
        except Exception:
            complain_and_abort(
                f"Failed to load dbt manifest from {self.dbt_manifest_path}."
            )

    def _resolve_dbt_ref(self, match, project_delimiter: str = ":"):
        model = match.group(1)
        node = self.dbt_nodes.get(f"model.{self.dbt_project}.{model}")
        if not node:
            complain_and_abort(f"Could not resolve dbt ref for {model}.")

        database = node["database"]
        schema = node["schema"]
        name = node.get("alias") or node["name"]

        return f"{database}{project_delimiter}{schema}.{name}"

    def _resolve_sql_dbt_ref(self, match):
        # We use BQ `:` internally, but other warehouses use `.` so for SQL we need to
        # avoid using `:`. BQ supports `.` as well as `:` so we can just always use `.`.
        return self._resolve_dbt_ref(match, project_delimiter=".")

    def _resolve_templates(self, yaml_object, ref_resolver: Optional[Callable] = None):
        ref_resolver = ref_resolver or self._resolve_dbt_ref

        if isinstance(yaml_object, str):
            return self.DBT_REF_PATTERN.sub(ref_resolver, yaml_object)
        elif isinstance(yaml_object, list):
            return [self._resolve_templates(i, ref_resolver) for i in yaml_object]
        elif isinstance(yaml_object, dict):
            return {
                k: self._resolve_templates(
                    v,
                    self._resolve_sql_dbt_ref if k in self.SQL_KEYS else ref_resolver,
                )
                for k, v in yaml_object.items()
            }

        return yaml_object

    @manage_errors
    def delete(self, namespace: str, dry_run: bool = False, abort_on_error=True):
        """
        Delete all monitors in namespace
        """
        response = self.client.delete_config_template(namespace, dry_run=dry_run)

        dry_run_s = "[DRY RUN] " if dry_run else ""
        self._print_func(
            f"\n{dry_run_s}Deleted {response.num_deleted} "
            f"resources in namespace={namespace}\n"
        )

        return response

    @manage_errors
    def list_namespaces(self, limit=100):
        """
        Get all namespaces
        """
        query = Query()
        templates = query.get_monte_carlo_config_templates(first=limit + 1)
        assert templates.edges is not None
        templates.edges.node.__fields__("namespace", "last_update_time")
        response = self._pycarlo_client(query)
        namespaces = [
            (edge.node.namespace, edge.node.last_update_time)
            for edge in response.get_monte_carlo_config_templates.edges  # type: ignore
            if edge.node is not None
        ]

        more_ns_available = False
        if len(namespaces) > limit:
            namespaces = namespaces[:-1]
            more_ns_available = True
        self._print_func(
            tabulate(namespaces, headers=self.NS_HEADERS, tablefmt="fancy_grid")
        )

        if more_ns_available:
            self._print_func(self.MORE_NS_MESSAGE)

    @manage_errors
    def generate_from_dbt_tests(
        self,
        output_path: str,
        test_types: Optional[List[str]] = None,
        labels: Optional[List[str]] = None,
    ):
        """
        Create Monte Carlo monitor config YAML from dbt tests in dbt manifest.
        May specify a subset of dbt test types to import.
        """
        tests = (
            n
            for n in self._load_dbt_manifest_nodes().values()
            if n.get("resource_type") == "test"
        )

        if test_types:
            test_type_set = set(test_types)
            tests = (
                t
                for t in tests
                if t.get("test_metadata", {}).get("name", "SINGULAR") in test_type_set
                # Singular tests do not have metadata
            )

        common_args = {
            "schedule": {
                "type": "fixed",
                "start_time": datetime.now(timezone.utc).isoformat(),
                "interval_minutes": 720,
            },
            "comparisons": [
                {"type": "threshold", "operator": "GT", "threshold_value": 0}
            ],
        }

        if labels:
            common_args["labels"] = sorted(list(set(labels)))

        custom_sql_rules = [
            {
                "name": t["unique_id"],
                "description": t["unique_id"],
                "sql": t["compiled_code"].strip(),
                **common_args,
            }
            for t in tests
        ]

        self._print_func(f"Found {len(custom_sql_rules)} dbt tests.")

        Box({"montecarlo": {"custom_sql": custom_sql_rules}}).to_yaml(
            output_path, sort_keys=False, width=float("inf")
        )

        self._print_func(f"Wrote monitor config to {output_path}.")

    @staticmethod
    def _str_presenter(dumper, data):
        # Configures yaml for dumping multiline strings
        if data.count("\n") > 0:
            # It is a multiline string. Use a | style
            return dumper.represent_scalar(
                tag="tag:yaml.org,2002:str",
                value=MonteCarloConfigService._prepare_multiline_str(data),
                style="|",
            )

        return dumper.represent_scalar("tag:yaml.org,2002:str", data)

    @staticmethod
    def _prepare_multiline_str(data: str) -> str:
        """
        Prepare the data to format as multiline string in the YAML. It must meet
        some conditions to represent it as a block by yaml.dump,
        """

        # Trailing spaces are not permitted (check analyze_scalar in emitter.py,
        # and how allow_block is defined)
        result = "\n".join([line.rstrip() for line in data.splitlines()])
        if not result.endswith("\n"):
            # Add a line break at the end (to avoid using |- and use | in the yaml)
            result += "\n"

        return result
