# Copyright (c) 2023 Henix, Henix.fr
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Selectors helpers"""

from typing import Any, Dict, List, Optional, Set, Tuple, Union

import re

########################################################################
## Constants

Object = Dict[str, Any]
OpCode = Tuple[
    int,
    Optional[Union[str, List[str]]],
    Optional[bool],
    Optional[Union[str, Set[str]]],
]

KEY = r'[a-z0-9A-Z-_./]+'
VALUE = r'[a-z0-9A-Z-_./@]+'
EQUAL_EXPR = re.compile(rf'^({KEY})\s*([=!]?=)\s*({VALUE})(?:,|$)')
SET_EXPR = re.compile(rf'^({KEY})\s+(in|notin)\s+\(({VALUE}(\s*,\s*{VALUE})*)\)(?:,|$)')
EXISTS_EXPR = re.compile(rf'^({KEY})(?:,|$)')
NEXISTS_EXPR = re.compile(rf'^!({KEY})(?:,|$)')


########################################################################
## Selectors helpers

OP_RESOLV = 0x01
OP_EQUAL = 0x10
OP_EXIST = 0x20
OP_NEXIST = 0x40
OP_SET = 0x80


def compile_selector(exprs: str, resolve_path: bool = True) -> List[OpCode]:
    """Compile selector.

    # Required parameters

    - exprs: a string, a comma-separated list of expressions

    # Optional parameters

    - resolve_path: a boolean, default True

    # Returned value

    A list of tuples, the 'compiled' selectors.

    # Raised exceptions

    A _ValueError_ exception is raised if at least one expression is
    invalid.
    """

    def _opcode(code, item, third=None, fourth=None):
        if resolve_path and '.' in item:
            return code | OP_RESOLV, item.split('.'), third, fourth
        return code, item, third, fourth

    compiled = []
    while exprs:
        if match := EQUAL_EXPR.match(exprs):
            key, ope, value = match.groups()
            instr = _opcode(OP_EQUAL, key, ope == '!=', value)
        elif match := EXISTS_EXPR.match(exprs):
            instr = _opcode(OP_EXIST, match.group(1))
        elif match := NEXISTS_EXPR.match(exprs):
            instr = _opcode(OP_NEXIST, match.group(1))
        elif match := SET_EXPR.match(exprs):
            key, ope, vals, _ = match.groups()
            instr = _opcode(
                OP_SET, key, ope == 'notin', {v.strip() for v in vals.split(',')}
            )
        else:
            raise ValueError(f'Invalid expression {exprs}.')
        compiled.append(instr)
        exprs = exprs[match.end() :].strip(', ')

    return compiled


def _resolve_path(items: List[str], obj) -> Tuple[bool, Optional[Any]]:
    head, rest = items[0], items[1:]
    if head in obj:
        return (True, obj[head]) if not rest else _resolve_path(rest, obj[head])
    return False, None


def _evaluate(req: OpCode, obj: Object) -> bool:
    """Evaluate whether req matches labels.

    # Required parameters

    - req: a tuple (a 'compiled' selector)
    - labels: a dictionary

    # Returned value

    A boolean.  True if `req` is satisfied by `obj`, False otherwise.
    """
    opcode, key, neq, arg = req
    if opcode == OP_EQUAL:  # fast path
        if key in obj:
            return (obj[key] == arg) ^ neq
        return neq  # type: ignore

    if opcode & OP_RESOLV:
        found, value = _resolve_path(key, obj)  # type: ignore
    else:
        found, value = key in obj, obj.get(key)  # type: ignore

    if opcode & OP_EXIST:
        return found

    if opcode & OP_NEXIST:
        return not found

    if found and opcode & OP_EQUAL:
        return (value == arg) ^ neq
    if found:  # OP_SET
        return (value in arg) ^ neq  # type: ignore
    return neq  # type: ignore


def match_field_compiledselector(obj: Object, opcodes: List[OpCode]) -> bool:
    return all(_evaluate(opcode, obj) for opcode in opcodes)


def match_label_compiledselector(obj: Object, opcodes: List[OpCode]) -> bool:
    labels = obj.get('metadata', {}).get('labels', {})
    return all(_evaluate(opcode, labels) for opcode in opcodes)


def match_field_selector(obj: Object, selector: str) -> bool:
    """Check if the object matches the selector.

    An empty selector always matches.

    The complete selector feature has been implemented.  `selector` is
    of form:

        expr[,expr]*

    where `expr` is one of `key`, `!key`, or `key op value`, with
    `op` being one of `=`, `==`, or `!=`.  The
    `key in (value[, value...])` and `key notin (value[, value...])`
    set-based requirements are also implemented.

    # Required parameters

    - obj: a message (a dictionary)
    - selector: a string

    # Returned value

    A boolean.

    # Raised exceptions

    A _ValueError_ exception is raised if `selector` is not a valid.
    """
    return match_field_compiledselector(obj, compile_selector(selector))


def match_label_selector(obj: Object, selector: str) -> bool:
    """Check if the message's labels match the selector.

    An empty selector always matches.

    The complete selector feature has been implemented.  `selector` is
    of form:

        expr[,expr]*

    where `expr` is one of `key`, `!key`, or `key op value`, with
    `op` being one of `=`, `==`, or `!=`.  The
    `key in (value[, value...])` and `key notin (value[, value...])`
    set-based requirements are also implemented.

    # Required parameters

    - obj: a message (a dictionary)
    - selector: a string

    # Returned value

    A boolean.

    # Raised exceptions

    A _ValueError_ exception is raised if `selector` is not a valid.
    """
    return match_label_compiledselector(
        obj, compile_selector(selector, resolve_path=False)
    )


def match_selectors(
    obj: Object,
    fieldselector: Union[None, str, List[OpCode]] = None,
    labelselector: Union[None, str, List[OpCode]] = None,
) -> bool:
    """Check if object matches selector.

    An empty selector matches.  The selectors can be strings or
    compiled selectors.

    # Required parameters

    - obj: a dictionary

    # Optional parameters

    - fieldselector: a string or a list of opcodes or None
    - labelselector: a string or a list of opcodes or None

    # Returned value

    A boolean.

    # Raised exceptions

    A _ValueError_ exception is raised if `fieldselector` or
    `labelselector` is not a valid.
    """
    if isinstance(fieldselector, str):
        fieldselector = compile_selector(fieldselector)
    if isinstance(labelselector, str):
        labelselector = compile_selector(labelselector, resolve_path=False)
    return (not fieldselector or match_field_compiledselector(obj, fieldselector)) and (
        not labelselector or match_label_compiledselector(obj, labelselector)
    )
