# -*- coding: utf-8 -*-
#################################|###|#####################################
#  __                            |   |                                    #
# |  |--.--.--.----.-----.-----. |===| This file is part of byron v0.1    #
# |  _  |  |  |   _|  _  |     | |___| An evolutionary optimizer & fuzzer #
# |_____|___  |__| |_____|__|__|  ).(  https://github.com/squillero/byron #
#       |_____|                   \|/                                     #
################################## ' ######################################

# Copyright 2023 Giovanni Squillero and Alberto Tonda
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
# v1 / April 2023 / Squillero (GX)

__all__ = ["sequence", "alternative", "bunch"]

from collections import abc
from typing import Sequence

from byron.global_symbols import *
from byron.user_messages import *
from byron.tools.names import canonize_name, _patch_class_info
from byron.classes.selement import SElement
from byron.classes.frame import *
from byron.classes.macro import Macro
from byron.framework.macro import macro
from byron.framework.utilities import cook_sequence
from byron.randy import rrandom


def alternative(
    alternatives: abc.Collection[type[SElement]], *, name: str | None = None, extra_parameters: dict = None
) -> type[FrameABC]:
    r"""Creates the class for a frame that can have alternative forms.

    An ``alternative`` is a frame that can take different forms,

    The `alternatives` is the collection of different forms, either ``FrameABC` or
    `Macro`. The different forms are atomic and equally probable.

    The `name` identifies the frame, allowing to refer to it in other portions of the code.

    The `parameters` is a dictionary of parameters that are made available to the frame and
    to all its successors in the structure tree.

    Parameters
    ----------
    alternatives : collection
        the possible alternatives.
    name : str, optional
        the name of the frame.
    extra_parameters : dict, optional
        dictionary of parameters.

    Returns
    -------
    FrameABC
        A class frame.

    Examples
    --------
    The definition of an expression in prefix notation::

        <expr> ::= <term> | <op> <expr> <expr>
        <op>   ::= '+' | '-' | '*' | '/'
        <term> ::= <num> | <var>
        <num>  ::= 0-999
        <var>  ::= 'x' | 'y' | 'z'

    In byron, `num` and `var` are macros; `term`, a frame; and `expr`, the bnf frame.

    >>> var = macro('{v}', v=choice_parameter('xyz'))
    >>> num = macro('{n}', n=integer_parameter(0, 1000))
    >>> term = alternative([var, num])
    >>> op = macro('{o}', o=choice_parameter('+-*/'))
    >>> expr = bnf([[term], [op, SELF, SELF]])

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form
    """
    assert check_valid_type(alternatives, abc.Collection)
    assert all(check_valid_types(a, FrameABC, Macro, subclass=True) for a in alternatives)
    assert check_valid_length(alternatives, 1)

    class T(FrameAlternative, FrameABC):
        ALTERNATIVES = tuple(alternatives)

        def __init__(self):
            super().__init__(extra_parameters)

        @property
        def successors(self):
            return [rrandom.choice(T.ALTERNATIVES)]

    if name:
        _patch_class_info(T, canonize_name(name, "Frame", user=True), tag=FRAMEWORK)
    else:
        _patch_class_info(T, canonize_name("FrameAlternative", "Frame"), tag=FRAMEWORK)

    FRAMEWORK_DIRECTORY[T.__name__] = T
    return T


def sequence(
    seq: abc.Sequence[type[SElement] | str], *, name: str | None = None, extra_parameters: dict = None
) -> type[FrameABC]:
    cooked_seq = cook_sequence(seq)

    class T(FrameSequence, FrameABC):
        SEQUENCE = tuple(cooked_seq)

        def __init__(self):
            super().__init__(extra_parameters)

        @property
        def successors(self):
            return T.SEQUENCE

    if name:
        _patch_class_info(T, canonize_name(name, "Frame", user=True), tag=FRAMEWORK)
    else:
        _patch_class_info(T, canonize_name("FrameSequence", "Frame"), tag=FRAMEWORK)

    FRAMEWORK_DIRECTORY[T.__name__] = T
    return T


def bunch(
    pool: Macro | abc.Collection[type[Macro]],
    size: tuple[int, int] | int = 1,
    *,
    name: str | None = None,
    weights: Sequence[int] | None = None,
    extra_parameters: dict = None,
) -> type[FrameABC]:
    def _debug_hints():
        if not isinstance(size, int) and size[0] + 1 == size[1]:
            syntax_warning_hint(
                f"Ranges are half open: the size of this macro bunch is always {size[0]} — did you mean 'size=({size[0]}, {size[1]+1})'?",
                stacklevel_offset=1,
            )
        if len(pool) > len(set(pool)):
            syntax_warning_hint(
                f"Found duplicate macros in pool — considering using 'weights'",
                stacklevel_offset=1,
            )
        return True

    assert check_valid_types(size, int, abc.Collection)
    assert (
        (not isinstance(pool, abc.Collection) and check_valid_type(pool, Macro, subclass=True))
        or isinstance(pool, abc.Collection)
        and (not pool or any(check_valid_type(t, Macro, subclass=True) for t in pool))
    )
    if isinstance(pool, type) and issubclass(pool, Macro):
        pool = [pool]
    assert check_valid_length(pool, 1)

    if isinstance(size, int):
        size = (size, size + 1)
    else:
        size = tuple(size)
        assert len(size) == 2, f"{PARANOIA_VALUE_ERROR}: Not a half open range [min, max)"
    assert 0 < size[0] <= size[1] - 1, f"{PARANOIA_VALUE_ERROR}: min size is {size[0]} and max size is {size[1]-1}"

    assert _debug_hints()

    if weights is None:
        weights = [1] * len(pool)

    class T(FrameMacroBunch, FrameABC):
        SIZE = size
        POOL = tuple(sum(([m] * w for m, w in zip(pool, weights)), start=list()))

        __slots__ = []  # Preventing the automatic creation of __dict__

        def __init__(self):
            super().__init__(extra_parameters)

        @property
        def successors(self):
            n_macros = rrandom.randint(T.SIZE[0], T.SIZE[1] - 1)
            return [rrandom.choice(T.POOL) for _ in range(n_macros)]

    def check_out_degree(n):
        return n.framework_out_degree >= size[0] and n.framework_out_degree < size[1]

    T.add_node_check(check_out_degree)

    # White parentheses: ⦅ ⦆  (U+2985, U+2986)
    if name:
        canonic_name = canonize_name(name, "Frame", user=True)
    elif size == (1, 2):
        canonic_name = canonize_name("SingleMacro", "Frame")
    elif size[1] - size[0] == 1:
        canonic_name = canonize_name("MacroArray", "Frame")
    else:
        canonic_name = canonize_name("MacroBunch", "Frame")
    _patch_class_info(T, canonic_name, tag=FRAMEWORK)

    FRAMEWORK_DIRECTORY[T.__name__] = T
    return T
