# This file is part of pipe_base.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (http://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Module defining few methods to manipulate or query pipelines.
"""

from __future__ import annotations

# No one should do import * from this module
__all__ = ["isPipelineOrdered", "orderPipeline"]

from collections.abc import Iterable
from typing import TYPE_CHECKING

from .pipeline import Pipeline, TaskDef

# Exceptions re-exported here for backwards compatibility.
from .pipeline_graph import DuplicateOutputError, PipelineDataCycleError, PipelineGraph  # noqa: F401

if TYPE_CHECKING:
    from .taskFactory import TaskFactory


class MissingTaskFactoryError(Exception):
    """Exception raised when client fails to provide TaskFactory instance."""

    pass


def isPipelineOrdered(pipeline: Pipeline | Iterable[TaskDef], taskFactory: TaskFactory | None = None) -> bool:
    """Check whether tasks in pipeline are correctly ordered.

    Pipeline is correctly ordered if for any DatasetType produced by a task
    in a pipeline all its consumer tasks are located after producer.

    Parameters
    ----------
    pipeline : `Pipeline` or `collections.abc.Iterable` [ `TaskDef` ]
        Pipeline description.
    taskFactory: `TaskFactory`, optional
        Ignored; present only for backwards compatibility.

    Returns
    -------
    is_ordered : `bool`
        True for correctly ordered pipeline, False otherwise.

    Raises
    ------
    ImportError
        Raised when task class cannot be imported.
    DuplicateOutputError
        Raised when there is more than one producer for a dataset type.
    """
    if isinstance(pipeline, Pipeline):
        graph = pipeline.to_graph()
    else:
        graph = PipelineGraph()
        for task_def in pipeline:
            graph.add_task(task_def.label, task_def.taskClass, task_def.config, task_def.connections)
    # Can't use graph.is_sorted because that requires sorted dataset type names
    # as well as sorted tasks.
    tasks_xgraph = graph.make_task_xgraph()
    seen: set[str] = set()
    for task_label in tasks_xgraph:
        successors = set(tasks_xgraph.successors(task_label))
        if not successors.isdisjoint(seen):
            return False
        seen.add(task_label)
    return True


def orderPipeline(pipeline: Pipeline | Iterable[TaskDef]) -> list[TaskDef]:
    """Re-order tasks in pipeline to satisfy data dependencies.

    Parameters
    ----------
    pipeline : `Pipeline` or `collections.abc.Iterable` [ `TaskDef` ]
        Pipeline description.

    Returns
    -------
    ordered : `list` [ `TaskDef` ]
        Correctly ordered pipeline.

    Raises
    ------
    DuplicateOutputError
        Raised when there is more than one producer for a dataset type.
    PipelineDataCycleError
        Raised when the pipeline has dependency cycles.
    """
    if isinstance(pipeline, Pipeline):
        graph = pipeline.to_graph()
    else:
        graph = PipelineGraph()
        for task_def in pipeline:
            graph.add_task(task_def.label, task_def.taskClass, task_def.config, task_def.connections)
    graph.sort()
    return list(graph._iter_task_defs())
