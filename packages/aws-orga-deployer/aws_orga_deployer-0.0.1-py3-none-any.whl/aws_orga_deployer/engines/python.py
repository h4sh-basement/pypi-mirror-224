"""Engine for Python modules."""
from os import path
from typing import Any, Dict, List

from aws_orga_deployer.engines import base
from aws_orga_deployer.package.store import ModuleAccountRegionKey


class Engine(base.BaseEngine):
    """Engine for Python modules."""

    engine = "python"
    default_included_patterns = ["*.py"]
    default_excluded_patterns = []

    def prepare(
        self,
        key: ModuleAccountRegionKey,
        command: str,
        action: str,
        variables: Dict[str, Any],
        module_config: Dict[str, Any],
        deployment_cache_dir: str,
        engine_cache_dir: str,
    ) -> List[base.StepCommand]:
        """Create a file `input.json` that contains input parameters, and return
        a command that executes the Python module script in a "wrapper" function.

        Args:
            key: Step key to execute.
            command: CLI command requested ("preview" or "deploy").
            action: Action to be made ("create", "update" or "destroy").
            variables: Input variables.
            module_config: Module configuration.
            deployment_cache_dir: Path to the module deployment cache directory.
            engine_cache_dir: Path to the engine cache directory (common to all
                modules for this engine).

        Returns:
            List of commands to execute in subprocesses.
        """
        # Write the inputs to a JSON file that the wrapper function can read
        self.write_wrapper_inputs(
            key,
            command,
            action,
            variables,
            module_config,
            deployment_cache_dir,
            engine_cache_dir,
        )
        # Locate the Python wrapper script that is executed in a subprocess
        wrapper_file = path.join(
            path.dirname(path.abspath(__file__)), "wrappers", "python.py"
        )
        # Locate the main script of the module
        module_file = path.join(self.module_dir, "main.py")
        # Return a command that execute the wrapper function with the path to
        # the module main script as an argument, and the worker cache folder as
        # the current working directory
        python_exec = base.get_python_executable(module_config)
        return [
            base.StepCommand(
                name="wrapper",
                args=[python_exec, wrapper_file, module_file],
                cwd=deployment_cache_dir,
                assume_role=True,
            )
        ]

    def postprocess(
        self,
        key: ModuleAccountRegionKey,
        command: str,
        action: str,
        module_config: Dict[str, Any],
        deployment_cache_dir: str,
    ) -> base.StepOutcome:
        """Reads the file `output.json` created by the "wrapper" function and
        returns the outputs.

        Args:
            key: Step key to execute.
            command: CLI command requested.
            action: Action to be made ("create", "update", "destroy").
            module_config: Module configuration.
            deployment_cache_dir: Path to the module deployment cache directory.

        Returns:
            Outcome of the step.
        """
        return self.read_wrapper_outputs(deployment_cache_dir)
