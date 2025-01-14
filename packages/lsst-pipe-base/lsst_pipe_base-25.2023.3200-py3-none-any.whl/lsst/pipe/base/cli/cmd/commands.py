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

from typing import Any

import click
from lsst.daf.butler.cli.opt import (
    options_file_option,
    register_dataset_types_option,
    repo_argument,
    transfer_dimensions_option,
)
from lsst.daf.butler.cli.utils import ButlerCommand

from ... import script
from ..opt import instrument_argument, update_output_chain_option


@click.command(short_help="Add an instrument definition to the repository", cls=ButlerCommand)
@repo_argument(required=True)
@instrument_argument(required=True, nargs=-1, help="The fully-qualified name of an Instrument subclass.")
@click.option("--update", is_flag=True)
def register_instrument(*args: Any, **kwargs: Any) -> None:
    """Add an instrument to the data repository."""
    script.register_instrument(*args, **kwargs)


@click.command(short_help="Transfer datasets from a graph to a butler.", cls=ButlerCommand)
@click.argument("graph", required=True)
@click.argument("dest", required=True)
@register_dataset_types_option()
@transfer_dimensions_option()
@update_output_chain_option()
@options_file_option()
def transfer_from_graph(**kwargs: Any) -> None:
    """Transfer datasets from a quantum graph to a destination butler.

    SOURCE is a URI to the Butler repository containing the RUN dataset.

    DEST is a URI to the Butler repository that will receive copies of the
    datasets.
    """
    number = script.transfer_from_graph(**kwargs)
    print(f"Number of datasets transferred: {number}")
