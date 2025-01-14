# Copyright (c) 2021 Henix, Henix.fr
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

"""Toolkit core functions."""


from typing import Any, Dict, Iterable, NoReturn, Optional

import inspect
import ntpath
import posixpath
import sys

from opentf.commons import (
    PROVIDERRESULT,
    EXECUTIONERROR,
    publish,
    make_event,
    make_uuid,
)


########################################################################
# Default Plugin registration

DEFAULT_PLUGIN = None


def register_defaultplugin(plugin) -> None:
    """Register default plugin.

    The core helpers assume a plugin context is defined.  If no plugin
    is found while searching the frames, the registered default plugin
    is used.
    """
    global DEFAULT_PLUGIN
    DEFAULT_PLUGIN = plugin


def deregister_defaultplugin(plugin) -> None:
    """Deregister default plugin."""
    global DEFAULT_PLUGIN
    if DEFAULT_PLUGIN == plugin:
        DEFAULT_PLUGIN = None


########################################################################
# Local helpers


def _getlocal(val: Optional[Any], name: str) -> Any:
    if val is None:
        if name == 'plugin':
            return DEFAULT_PLUGIN
        raise SystemError('No previous frame, should not happen, aborting.')
    if name in val.f_locals:
        return val.f_locals[name]
    return _getlocal(val.f_back, name)


def _getplugin() -> Any:
    return _getlocal(inspect.currentframe(), 'plugin')


def _getbody() -> Dict[str, Any]:
    return _getlocal(inspect.currentframe(), 'body')


def _getcontexts() -> Any:
    return _getbody()['contexts']


def _getstep() -> Dict[str, Any]:
    return _getbody()['step']


########################################################################
## Exception helpers


class ExecutionError(Exception):
    """An ExecutionError exception.

    Only expected to be raised in a workflow thread.  Will publish
    the corresponding ExecutionError event if in this context.
    """

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return str(self.message)


########################################################################
## Publication helpers


def publish_event(event) -> None:
    """Publish event."""
    publish(event, context=_getplugin().config['CONTEXT'])


def publish_error(error_details) -> None:
    """Publish ExecutionError event."""
    error = make_event(
        EXECUTIONERROR,
        metadata=_getbody()['metadata'],
        details={'error': error_details},
    )
    publish_event(error)


def publish_providerresult(steps: Iterable) -> None:
    """Publish ProviderResult event."""
    command = make_event(
        PROVIDERRESULT,
        metadata=_getbody()['metadata'],
        steps=[step.copy() for step in steps],
    )
    if hooks := _getplugin().config['CONFIG'].get('hooks'):
        command['hooks'] = hooks
    for step in command['steps']:
        step.setdefault('id', make_uuid())
    publish_event(command)


########################################################################
## Toolkit helpers


def debug(*msg) -> None:
    """Log debug message."""
    _getplugin().logger.debug(*msg)


def info(*msg) -> None:
    """Log info message."""
    _getplugin().logger.info(*msg)


def warning(*msg) -> None:
    """Log warning message."""
    _getplugin().logger.warning(*msg)


def error(*msg) -> None:
    """Log error message."""
    _getplugin().logger.error(*msg)


def fatal(*msg) -> NoReturn:
    """Log error message and exit with error code 2."""
    error(*msg)
    sys.exit(2)


def fail(error_details: str):
    """Raise an ExecutionError event."""
    raise ExecutionError(error_details)


def runner_on_windows() -> bool:
    """Check if execution environment is windows-based."""
    return _getcontexts().get('runner', {}).get('os') == 'windows'


def normalize_path(path: str) -> str:
    """Normalize path.

    If the execution environment is windows-based, forward slashes will
    be replaced by backward slashes.

    If spaces are found in path, it will be surrounded by double quotes.
    """
    if runner_on_windows():
        path = ntpath.normpath(path)
    else:
        path = posixpath.normpath(path)
    if ' ' in path:
        return f'"{path}"'
    return path


def join_path(path1: str, path2: Optional[str], runner_on_windows: bool) -> str:
    """Join two paths.

    If the execution environment is windows-based, forward slashes will
    be replaced by backward slashes.

    No attempt is made to ensure operation makes sense.

    If `path2` is None, returns `path1`.
    """
    if path2 is None:
        if runner_on_windows:
            return ntpath.normpath(path1)
        return posixpath.normpath(path1)

    if runner_on_windows:
        return ntpath.normpath(ntpath.join(path1, path2))
    return posixpath.join(path1, path2)


## Steps


def set_secret(secret: str) -> str:
    """Set secret.

    The secret will be hidden in warning/debug/error outputs.
    """
    if runner_on_windows():
        return f'@echo ::add-mask::{secret}'
    return f'echo "::add-mask::{secret}"'


def export_variable(name: str, value: str) -> str:
    """Export variable.

    The variable will be visible by following steps.
    """
    if runner_on_windows():
        return f'@echo set "{name}={value}" >>"%OPENTF_VARIABLES%"'
    if ' ' in value:
        value = f'\\"{value}\\"'
    return f'echo export {name}={value} >> "$OPENTF_VARIABLES"'


def attach_file(path: str, **kwargs) -> str:
    """Attach file.

    `path` is a relative file path (from the current directory)

    `kwargs` are key/value pairs that are added as workflow command
    parameters:

    ```python
    core.attach_file('/foo/bar.xml',type='text/xml', charset='utf8')
    # gives ::attach type=text/xml, charset=utf-8::/foo/bar.xml
    """
    if kwargs:
        parameters = ' ' + ','.join(f'{key}={value}' for key, value in kwargs.items())
    else:
        parameters = ''

    if runner_on_windows():
        path = ntpath.normpath(path)
        return f'@echo ::attach{parameters}::%CD%\\{path}'
    return f'echo "::attach{parameters}::`pwd`/{path}"'


def delete_file(path: str) -> str:
    """Delete file."""
    path = normalize_path(path)
    if runner_on_windows():
        return f'@if exist {path} @del /f/q {path}'
    return f'rm -f {path}'


def delete_directory(path: str) -> str:
    """Delete directory."""
    path = normalize_path(path)
    if runner_on_windows():
        return f'@if exist {path} @rmdir /s/q {path}'
    return f'rm -rf {path}'


def touch_file(path: str) -> str:
    """Touch file."""
    path = normalize_path(path)
    if runner_on_windows():
        return f'@type nul >>{path}'
    return f'touch {path}'
