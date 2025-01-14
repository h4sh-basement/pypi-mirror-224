"""
A class to run a pipeline.
"""
from typing import Any, Dict, Optional, Union

from hyfi.task import TaskConfig
from hyfi.utils.logging import LOGGING
from hyfi.workflow import WorkflowConfig

from .config import PipeConfig, PipelineConfig, run_pipe

logger = LOGGING.getLogger(__name__)


class PIPELINEs:
    """
    A class to run a pipeline.
    """

    @staticmethod
    def run_pipeline(
        config: Union[Dict, PipelineConfig],
        initial_object: Optional[Any] = None,
        task: Optional[TaskConfig] = None,
    ) -> Any:
        """
        Run a pipeline given a config

        Args:
            config: PipelineConfig to run the pipeline
            initial_obj: Object to use as initial value
            task: TaskConfig to use as task

        Returns:
            The result of the pipeline
        """
        if task is None:
            task = TaskConfig()
        return task.run_pipeline(config, initial_object)

    @staticmethod
    def run_pipe(
        obj: Any,
        config: Union[Dict, PipeConfig],
    ) -> Any:
        """
        Run a pipe on an object

        Args:
            obj: The object to pipe on
            config: The configuration for the pipe

        Returns:
            The result of the pipe
        """
        return run_pipe(obj, config)

    @staticmethod
    def run_task(
        task: TaskConfig,
        dryrun: bool = False,
    ):
        """
        Run pipelines specified in the task

        Args:
            task: TaskConfig to run pipelines for
            project: ProjectConfig to run pipelines
        """
        if dryrun:
            print("\nDryrun is enabled, not running the HyFI task\n")
            return
        task.run()

    @staticmethod
    def run_workflow(workflow: WorkflowConfig, dryrun: bool = False):
        """
        Run the tasks specified in the workflow

        Args:
            workflow: WorkflowConfig object to run
        """
        if dryrun:
            print("\nDryrun is enabled, not running the HyFI workflow\n")
            return
        workflow.run()

    @staticmethod
    def pipe(**kwargs) -> PipeConfig:
        """
        Return the PipeConfig.

        Args:
            **kwargs: Additional keyword arguments to pass to the PipeConfig constructor.

        Returns:
            PipeConfig: An instance of the PipeConfig class.
        """
        return PipeConfig(**kwargs)
