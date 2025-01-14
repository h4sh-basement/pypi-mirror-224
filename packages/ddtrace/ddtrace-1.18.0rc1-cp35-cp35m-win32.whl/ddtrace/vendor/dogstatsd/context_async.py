# Unless explicitly stated otherwise all files in this repository are licensed under the BSD-3-Clause License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2015-Present Datadog, Inc
"""
Decorator `timed` for coroutine methods.

Warning: requires Python 3.5 or higher.
"""
# stdlib
import sys


# Wrap the Python 3.5+ function in a docstring to avoid syntax errors when
# running mypy in --py2 mode. Currently there is no way to have mypy skip an
# entire file if it has syntax errors. This solution is very hacky; another
# option is to specify the source files to process in mypy.ini (using glob
# inclusion patterns), and omit this file from the list.
#
# https://stackoverflow.com/a/57023749/3776794
# https://github.com/python/mypy/issues/6897
ASYNC_SOURCE = r'''
from functools import wraps
from time import time


def _get_wrapped_co(self, func):
    """
    `timed` wrapper for coroutine methods.
    """
    @wraps(func)
    async def wrapped_co(*args, **kwargs):
        start = time()
        try:
            result = await func(*args, **kwargs)
            return result
        finally:
            self._send(start)
    return wrapped_co
'''


def _get_wrapped_co(self, func):
    raise NotImplementedError(
        u"Decorator `timed` compatibility with coroutine functions"
        u" requires Python 3.5 or higher."
    )


if sys.version_info >= (3, 5):
    exec(compile(ASYNC_SOURCE, __file__, "exec"))
