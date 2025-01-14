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
from __future__ import annotations

from collections.abc import Iterable, Iterator, Mapping, Sequence
from typing import Any, ClassVar, TypeVar, cast, overload

import networkx

from ._dataset_types import DatasetTypeNode
from ._exceptions import UnresolvedGraphError
from ._nodes import NodeKey, NodeType
from ._tasks import TaskInitNode, TaskNode

_N = TypeVar("_N", covariant=True)
_T = TypeVar("_T")


class MappingView(Mapping[str, _N]):
    """Base class for mapping views into nodes of certain types in a
    `PipelineGraph`.


    Parameters
    ----------
    parent_xgraph : `networkx.MultiDiGraph`
        Backing networkx graph for the `PipelineGraph` instance.

    Notes
    -----
    Instances should only be constructed by `PipelineGraph` and its helper
    classes.

    Iteration order is topologically sorted if and only if the backing
    `PipelineGraph` has been sorted since its last modification.
    """

    def __init__(self, parent_xgraph: networkx.MultiDiGraph) -> None:
        self._parent_xgraph = parent_xgraph
        self._keys: list[str] | None = None

    _NODE_TYPE: ClassVar[NodeType]  # defined by derived classes

    def __contains__(self, key: object) -> bool:
        # The given key may not be a str, but if it isn't it'll just fail the
        # check, which is what we want anyway.
        return NodeKey(self._NODE_TYPE, cast(str, key)) in self._parent_xgraph

    def __iter__(self) -> Iterator[str]:
        if self._keys is None:
            self._keys = self._make_keys(self._parent_xgraph)
        return iter(self._keys)

    def __getitem__(self, key: str) -> _N:
        return self._parent_xgraph.nodes[NodeKey(self._NODE_TYPE, key)]["instance"]

    def __len__(self) -> int:
        if self._keys is None:
            self._keys = self._make_keys(self._parent_xgraph)
        return len(self._keys)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self!s})"

    def __str__(self) -> str:
        return f"{{{', '.join(iter(self))}}}"

    def _reorder(self, parent_keys: Sequence[NodeKey]) -> None:
        """Set this view's iteration order according to the given iterable of
        parent keys.

        Parameters
        ----------
        parent_keys : `~collections.abc.Sequence` [ `NodeKey` ]
            Superset of the keys in this view, in the new order.
        """
        self._keys = self._make_keys(parent_keys)

    def _reset(self) -> None:
        """Reset all cached content.

        This should be called by the parent graph after any changes that could
        invalidate the view, causing it to be reconstructed when next
        requested.
        """
        self._keys = None

    def _make_keys(self, parent_keys: Iterable[NodeKey]) -> list[str]:
        """Make a sequence of keys for this view from an iterable of parent
        keys.

        Parameters
        ----------
        parent_keys : `~collections.abc.Iterable` [ `NodeKey` ]
            Superset of the keys in this view.
        """
        return [str(k) for k in parent_keys if k.node_type is self._NODE_TYPE]


class TaskMappingView(MappingView[TaskNode]):
    """A mapping view of the tasks in a `PipelineGraph`.

    Notes
    -----
    Mapping keys are task labels and values are `TaskNode` instances.
    Iteration order is topological if and only if the `PipelineGraph` has been
    sorted since its last modification.
    """

    _NODE_TYPE = NodeType.TASK


class TaskInitMappingView(MappingView[TaskInitNode]):
    """A mapping view of the nodes representing task initialization in a
    `PipelineGraph`.

    Notes
    -----
    Mapping keys are task labels and values are `TaskInitNode` instances.
    Iteration order is topological if and only if the `PipelineGraph` has been
    sorted since its last modification.
    """

    _NODE_TYPE = NodeType.TASK_INIT


class DatasetTypeMappingView(MappingView[DatasetTypeNode]):
    """A mapping view of the nodes representing task initialization in a
    `PipelineGraph`.

    Notes
    -----
    Mapping keys are parent dataset type names and values are `DatasetTypeNode`
    instances, but values are only available for nodes that have been resolved
    (see `PipelineGraph.resolve`).  Attempting to access an unresolved value
    will result in `UnresolvedGraphError` being raised.  Keys for unresolved
    nodes are always present and iterable.

    Iteration order is topological if and only if the `PipelineGraph` has been
    sorted since its last modification.
    """

    _NODE_TYPE = NodeType.DATASET_TYPE

    def __getitem__(self, key: str) -> DatasetTypeNode:
        if (result := super().__getitem__(key)) is None:
            raise UnresolvedGraphError(f"Node for dataset type {key!r} has not been resolved.")
        return result

    def is_resolved(self, key: str) -> bool:
        """Test whether a node has been resolved."""
        return super().__getitem__(key) is not None

    @overload
    def get_if_resolved(self, key: str) -> DatasetTypeNode | None:
        ...  # pragma: nocover

    @overload
    def get_if_resolved(self, key: str, default: _T) -> DatasetTypeNode | _T:
        ...  # pragma: nocover

    def get_if_resolved(self, key: str, default: Any = None) -> DatasetTypeNode | Any:
        """Get a node or return a default if it has not been resolved.

        Parameters
        ----------
        key : `str`
            Parent dataset type name.
        default
            Value to return if this dataset type has not been resolved.

        Raises
        ------
        KeyError
            Raised if the node is not present in the graph at all.
        """
        if (result := super().__getitem__(key)) is None:
            return default  # type: ignore
        return result
