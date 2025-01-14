# -*- coding: utf-8 -*-
#############################################################################
#   __                          (`/\                                        #
#  |  |--.--.--.----.-----.-----`=\/\   This file is part of byron v0.1     #
#  |  _  |  |  |   _|  _  |     |`=\/\  An evolutionary optimizer & fuzzer  #
#  |_____|___  |__| |_____|__|__| `=\/  https://github.com/squillero/byron  #
#        |_____|                     \                                      #
#############################################################################
# Copyright 2022-23 Giovanni Squillero and Alberto Tonda
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.

# =[ HISTORY ]===============================================================
# v1 / May 2023 / Squillero (GX)

__all__ = ["MacroZero", "Info"]

import sys
from datetime import datetime

import networkx as nx

from byron.classes.macro import Macro
from byron.global_symbols import __version__ as version
from byron.tools.names import canonize_name, _patch_class_info
from byron.user_messages import *


class MacroZero(Macro):
    TEXT = (
        "{_comment}"
        + f""" Automagically generated by MicroGP v{version}"""
        + f""" on {datetime.today().strftime('%d-%b-%Y')}"""
        + f""" at {datetime.today().strftime('%H:%M:%S')}"""
    )
    EXTRA_PARAMETERS = dict()
    PARAMETERS = dict()

    @property
    def valid(self) -> bool:
        return True


class Info(Macro):
    import platform

    try:
        import psutil
    except ModuleNotFoundError:
        pass

    TEXT = "{_comment} [INFO] NOW: " + datetime.isoformat(datetime.now())
    TEXT += "\n{_comment} [INFO] Python: " + sys.version
    TEXT += "\n{_comment} [INFO] NetworkX: " + nx.__version__
    EXTRA_PARAMETERS = dict()

    system = "System: "
    try:
        system += f"{platform.machine()} ({platform.processor()}) "
    except NameError:
        pass
    try:
        system += f"{psutil.cpu_count(logical=False)} physical cores, {psutil.cpu_count(logical=True)} logical; {psutil.virtual_memory().total // 2 ** 20:,} MiB RAM"
    except NameError:
        pass
    TEXT += "\n{_comment} [INFO] " + system
    try:
        TEXT += "\n{_comment} [INFO] OS: " + str(platform.version())
    except NameError:
        pass

    _parameter_types = dict()

    @property
    def valid(self) -> bool:
        return True


_patch_class_info(
    MacroZero, canonize_name("MacroZero", "Macro", make_unique=False, warn_duplicates=False), tag="framework"
)
_patch_class_info(Info, canonize_name("Info", "Macro", make_unique=False, warn_duplicates=False), tag="framework")
