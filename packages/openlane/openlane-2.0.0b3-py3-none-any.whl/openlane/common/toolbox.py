# Copyright 2023 Efabless Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import re
import sys
import uuid
import fnmatch
import tempfile
import subprocess
from enum import IntEnum
from shutil import which
from typing import (
    Any,
    Callable,
    Dict,
    FrozenSet,
    Iterable,
    Mapping,
    Optional,
    Tuple,
    List,
    Union,
)

from deprecated.sphinx import deprecated

from .memoize import memoize
from .metrics import aggregate_metrics
from .generic_dict import is_string
from .misc import Path, mkdirp, get_script_dir
from .design_format import DesignFormat
from ..logging import debug, warn


class Toolbox(object):
    """
    An assisting object shared by a Flow and all its constituent Steps.

    The toolbox may create artifacts that are cached to avoid constant re-creation
    between steps.
    """

    def __init__(self, tmp_dir: str) -> None:
        self.tmp_dir = os.path.abspath(tmp_dir)

    @deprecated(
        version="2.0.0b1",
        reason="Use 'aggregate_metrics' from 'openlane.common'",
        action="once",
    )
    def aggregate_metrics(
        self,
        input: Dict[str, Any],
        aggregator_by_metric: Dict[str, Tuple[Any, Callable[[Iterable], Any]]],
    ) -> Dict[str, Any]:
        return aggregate_metrics(input, aggregator_by_metric)

    def filter_views(
        self,
        config: Mapping[str, Any],
        views_by_corner: Mapping[str, Union[Path, Iterable[Path]]],
        timing_corner: Optional[str] = None,
    ) -> List[Path]:
        """
        Given a mapping from (wildcards of) corner names to views, this function
        enumerates all views matching either the default timing corner or
        an explicitly-provided override.

        :param config: The configuration. Used solely to extract the default corner.
        :param views_by_corner: The mapping from (wild cards) of vorner names to
            views.
        :param corner: An explicit override for the default corner. Must be a
            fully qualified IPVT corner.
        :returns: The created list
        """
        timing_corner = timing_corner or config["DEFAULT_CORNER"]
        result: List[Path] = []

        for key, value in views_by_corner.items():
            if not fnmatch.fnmatch(timing_corner, key):
                continue
            if is_string(value):
                result += [value]  # type: ignore
            else:
                result += list(value)  # type: ignore

        return result

    def get_macro_views(
        self,
        config: Mapping[str, Any],
        view: DesignFormat,
        timing_corner: Optional[str] = None,
        unless_exist: Optional[DesignFormat] = None,
    ) -> List[Path]:
        """
        For :class:`Config` objects (or similar Mappings) that have Macro
        information, this function gets all Macro views matching a certain
        :class:`DesignFormat` for either the default timing corner or an
        explicitly-provided override.

        :param config: The configuration.
        :param view: The design format to return views of.
        :param timing_corner: An explicit override for the default corner set
            by the configuration.
        :param corner: An explicit override for the default corner. Must be a
            fully qualified IPVT corner.
        :param unless_exist: If a Macro also has a view for this DesignFormat,
            do not return a result for the requested DesignFormat.

            Useful for if you want to return say, Netlists if reliable LIB files
            do not exist.
        :returns: A list of the Macro views matched by the process described
            above.
        """
        from ..config import Macro

        timing_corner = timing_corner or config["DEFAULT_CORNER"]
        macros = config["MACROS"]
        result: List[Path] = []

        if macros is None:
            return result

        for module, macro in macros.items():
            if not isinstance(macro, Macro):
                raise TypeError(
                    f"Misconstructed configuration: macro definition for key {module} is not of type 'Macro'."
                )

            views = macro.view_by_df(view)
            if views is None:
                continue

            if unless_exist is not None:
                entry = macro.view_by_df(unless_exist)
                if entry is not None:
                    alt_views = entry
                    if isinstance(alt_views, dict):
                        alt_views = self.filter_views(config, alt_views, timing_corner)
                    elif not isinstance(alt_views, list):
                        alt_views = [alt_views]
                    if len(alt_views) != 0:
                        continue
            if isinstance(views, dict):
                views_filtered = self.filter_views(config, views, timing_corner)
                result += views_filtered
            elif isinstance(views, list):
                result += views
            elif views is not None and str(views) != "":
                result += [Path(views)]
        return result

    def get_timing_files(
        self,
        config: Mapping[str, Any],
        timing_corner: Optional[str] = None,
        prioritize_nl: bool = False,
    ) -> Tuple[str, List[str]]:
        """
        Returns the lib files for a given configuration and timing corner.

        :param config: A configuration object or a similar mapping.
        :param timing_corner: A fully qualified IPVT corner to get SCL libs for.

            If not specified, the value for `DEFAULT_CORNER` from the SCL will
            be used.
        :param prioritize_nl: Do not return lib files for macros that have
            Gate-Level Netlists and SPEF views.

            If set to ``false``, only lib files are returned.
        :returns: A tuple:
            - \\[0\\] being the name of the timing corner
            - \\[1\\] being a heterogenous list of files
                - Lib files are returned as-is
                - Netlists are returned as-is
                - SPEF files are returned in the format "{instance_name}@{spef_path}"

            It is left up to the step or tool to process this list as they see
            fit.
        """
        from ..config import Macro

        timing_corner = timing_corner or config["DEFAULT_CORNER"]

        result: List[Union[str, Path]] = []
        result += self.filter_views(config, config["LIB"], timing_corner)

        if len(result) == 0:
            warn(f"No SCL lib files found for {timing_corner}.")

        macros = config["MACROS"]
        if macros is None:
            macros = {}

        for module, macro in macros.items():
            if not isinstance(macro, Macro):
                raise TypeError(
                    f"Misconstructed configuration: macro definition for key {module} is not of type 'Macro'."
                )
            if prioritize_nl:
                netlists = macro.nl
                spefs = self.filter_views(
                    config,
                    macro.spef,
                    timing_corner,
                )
                if len(netlists) and not len(spefs):
                    warn(
                        f"Netlists found for macro {module}, but no parasitics extraction found at corner {timing_corner}. The netlist cannot be used for timing on this module."
                    )
                elif len(spefs) and not len(netlists):
                    warn(
                        f"Parasitics extraction(s) found for macro {module} at corner {timing_corner}, but no netlist found. The parasitics cannot be used for timing on this module."
                    )
                elif len(spefs) and len(netlists):
                    debug(f"Adding {[netlists + spefs]} to timing info…")
                    result += netlists
                    for spef in spefs:
                        for instance in macro.instances:
                            result.append(f"{instance}@{spef}")
                    continue
            # NL/SPEF not prioritized or not found
            libs = self.filter_views(
                config,
                macro.lib,
                timing_corner,
            )
            if not len(libs):
                warn(
                    f"No libs found for macro {module} at corner {timing_corner}. The module will be black-boxed."
                )
                continue
            debug(f"Adding {libs} to timing info…")
            result += libs

        return (timing_corner, [str(path) for path in result])

    def __render_common(
        self, config: Mapping[str, Any]
    ) -> Optional[Tuple[str, str, str]]:  # pragma: no cover
        klayout_bin = which("klayout")
        if klayout_bin is None:
            warn("This PDK does not support KLayout; previews cannot be rendered.")
            return None

        lyp = config["KLAYOUT_PROPERTIES"]
        lyt = config["KLAYOUT_TECH"]
        lym = config["KLAYOUT_DEF_LAYER_MAP"]
        if None in [lyp, lyt, lym]:
            warn("This PDK does not support KLayout; previews cannot be rendered.")
            return None
        return (str(lyp), str(lyt), str(lym))

    def render_png(
        self, config: Mapping[str, Any], input: str
    ) -> Optional[bytes]:  # pragma: no cover
        files = self.__render_common(config)
        if files is None:
            return None
        lyp, lyt, lym = files

        tech_lefs = self.filter_views(config, config["TECH_LEFS"])
        if len(tech_lefs) != 1:
            raise ValueError(
                "Misconfigured SCL: 'TECH_LEFS' must return exactly one Tech LEF for its default timing corner."
            )

        lef_arguments = ["-l", str(tech_lefs[0])]
        for file in config["CELL_LEFS"]:
            lef_arguments += ["-l", str(file)]
        if extra := config["EXTRA_LEFS"]:
            for file in extra:
                lef_arguments += ["-l", str(file)]

        result = None
        with tempfile.NamedTemporaryFile() as f:
            try:
                cmd = [
                    sys.executable,
                    os.path.join(get_script_dir(), "klayout", "render.py"),
                    input,
                    "--output",
                    f.name,
                    "--lyp",
                    lyp,
                    "--lyt",
                    lyt,
                    "--lym",
                    lym,
                ] + lef_arguments
                subprocess.check_output(
                    cmd,
                    stderr=subprocess.STDOUT,
                    encoding="utf8",
                )
                result = f.read()
            except subprocess.CalledProcessError as e:
                warn(f"Failed to render preview: {e.stdout}")
        return result

    @memoize()
    def remove_cells_from_lib(
        self,
        input_lib_files: FrozenSet[str],
        excluded_cells: FrozenSet[str],
        as_cell_lists: bool = False,
    ) -> List[str]:
        """
        Creates a new lib file with some cells removed.

        This function is memoized, i.e., results are cached for a specific set
        of inputs.

        :param input_lib_files: A `frozenset` of input lib files.
        :param excluded_cells: A `frozenset` of either cells to be removed or
            lists of cells to be removed if `as_cell_lists` is set to `True`.
        :param as_cell_lists: If set to true, `excluded_cells` is treated as a
            list of files that are themselves lists of cells. Otherwise, it is
            treated as a list of cells.
        :returns: A path to the lib file with the removed cells.
        """
        if as_cell_lists:  # Paths to files
            excluded_cells_str = ""
            for file in excluded_cells:
                excluded_cells_str += open(file, encoding="utf8").read()
                excluded_cells_str += "\n"
            excluded_cells = frozenset(
                [
                    cell.strip()
                    for cell in excluded_cells_str.strip().split("\n")
                    if cell.strip() != ""
                ]
            )

        class State(IntEnum):
            initial = 0
            cell = 10
            excluded_cell = 11

        cell_start_rx = re.compile(r"(\s*)cell\s*\(\"?(.*?)\"?\)\s*\{")

        mkdirp(self.tmp_dir)

        out_paths = []

        for file in input_lib_files:
            input_lib_stream = open(file)
            out_filename = f"{uuid.uuid4().hex}.lib"
            out_path = os.path.join(self.tmp_dir, out_filename)

            state = State.initial
            brace_count = 0
            output_file_handle = open(out_path, "w")
            write = lambda x: print(x, file=output_file_handle, end="")
            for line in input_lib_stream:
                if state == State.initial:
                    cell_m = cell_start_rx.search(line)
                    if cell_m is not None:
                        whitespace = cell_m[1]
                        cell_name = cell_m[2]
                        if cell_name in excluded_cells:
                            state = State.excluded_cell
                            write(f"{whitespace}/* removed {cell_name} */\n")
                        else:
                            state = State.cell
                            write(line)
                        brace_count = 1
                    else:
                        write(line)
                elif state in [State.cell, State.excluded_cell]:
                    if "{" in line:
                        brace_count += 1
                    if "}" in line:
                        brace_count -= 1
                    if state == State.cell:
                        write(line)
                    if brace_count == 0:
                        state = State.initial

            output_file_handle.close()

            out_paths.append(out_path)

        return out_paths
