"""
Mapper for any metric class and subclass.
"""

from typing import Any, Dict, Optional, Union

from nlgmetricverse.metrics._core.base import MetricForTask
from nlgmetricverse.metrics._core.utils import TaskNotAvailable
from nlgmetricverse.utils.string import camel_to_snake


class TaskMapper:
    """
    Base metric factory class which will be used as mapper for any metric class. This class is used by
    :py:class:`nlgmetricverse.AutoMetric` for loading specified metric. It maps the class to a specified metric class
    if multiple tasks are available for the metric.
    All metrics using TaskMapper must implement _TASKS attribute.
    Note:
        Use :py:class:`nlgmetricverse.metrics.TaskMapper` instead in case of metrics implementing a single task.
    """

    _TASKS: Dict[str, MetricForTask] = None

    def __init__(self, *args, **kwargs):
        raise EnvironmentError("This class is designed to be instantiated by using 'by_task()' method.")

    @classmethod
    def construct(
        cls, task: str, resulting_name: Optional[str] = None, compute_kwargs: Optional[Dict[str, Any]] = None, **kwargs
    ) -> MetricForTask:
        """
        Common interface for all metrics for specified MetricForTask to be constructed.

        :param task: Task name for the desired metric to obtain the subclass.
        :param resulting_name: Resulting name of the computed score returned. If None,`~._get_path()` is used.
        :param compute_kwargs: Arguments to be passed to `compute()` method of metric at computation.
        :param kwargs: Additional arguments used for the metric computation.
        :raises Exception: :py:class:`TaskNotAvailable`.
        :return: Metric for proper task if available.
        """
        subclass = cls._get_subclass(task=task)
        path = cls._get_path()
        resulting_name = resulting_name or path
        if subclass is None:
            raise TaskNotAvailable(path=path, task=task)
        return subclass._construct(resulting_name=resulting_name, compute_kwargs=compute_kwargs, **kwargs)

    @classmethod
    def _get_subclass(cls, task: str) -> Union[MetricForTask, None]:
        """
        All metric modules must implement this method as it is used to call metrics by default. Should raise
        proper exception (``TaskNotAvailable``) if the task is not supported by the metric.

        :param task: Task name for the desired metric.
        :return: Metric for proper task if available, None otherwise.
        """
        return cls._TASKS.get(task, None)

    @classmethod
    def _get_path(cls):
        return camel_to_snake(cls.__name__)


class MetricAlias(TaskMapper):
    """
    Extension of TaskMapper which allows a single :py:class:`nlgmetricverse.metrics.MetricForTask` class to be aliased.
    If a metric has a single task, use this class instead of :py:class:`nlgmetricverse.metrics._core.TaskMapper`.
    All metrics using MetricAlias must implement _SUBCLASS attribute.
    """

    _SUBCLASS: MetricForTask = None

    @classmethod
    def construct(
        cls,
        task: str = None,
        resulting_name: Optional[str] = None,
        compute_kwargs: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> MetricForTask:
        """
        Common interface for all metrics for specified MetricForTask to be constructed. Do not raise
        :py:class:`TaskNotAvailable` unlike :py:class:`TaskMapper` as it directly uses _SUBCLASS defined.

        :param task: Ignored. Preserved to provide a common interface.
        :param resulting_name: Resulting name of the computed score returned. If None, `~._get_path()` is used.
        :param compute_kwargs: Arguments to be passed to `compute()` method of metric at computation.
        :param kwargs: Additional arguments used for the metric computation.
        :return: Metric for proper task if available.
        """
        subclass = cls._get_subclass()
        resulting_name = resulting_name or cls._get_path()
        return subclass._construct(resulting_name=resulting_name, compute_kwargs=compute_kwargs, **kwargs)

    @classmethod
    def _get_subclass(cls, *args, **kwargs) -> MetricForTask:
        """
        Get metric subclass.

        :param args: Arguments to pass to the subclass
        :param kwargs: Additional arguments used for the metric computation.
        :return: Subclass metric for proper task.
        """
        return cls._SUBCLASS
