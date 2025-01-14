"""
The aioredis integration instruments aioredis requests. Version 1.3 and above are fully
supported.


Enabling
~~~~~~~~

The aioredis integration is enabled automatically when using
:ref:`ddtrace-run <ddtracerun>` or :func:`patch_all() <ddtrace.patch_all>`.

Or use :func:`patch() <ddtrace.patch>` to manually enable the integration::

    from ddtrace import patch
    patch(aioredis=True)


Global Configuration
~~~~~~~~~~~~~~~~~~~~

.. py:data:: ddtrace.config.aioredis["service"]

   The service name reported by default for aioredis instances.

   This option can also be set with the ``DD_AIOREDIS_SERVICE`` environment
   variable.

   Default: ``"redis"``

.. py:data:: ddtrace.config.aioredis["cmd_max_length"]

   Max allowable size for the aioredis command span tag.
   Anything beyond the max length will be replaced with ``"..."``.

   This option can also be set with the ``DD_AIOREDIS_CMD_MAX_LENGTH`` environment
   variable.

   Default: ``1000``


Instance Configuration
~~~~~~~~~~~~~~~~~~~~~~

To configure the aioredis integration on a per-instance basis use the
``Pin`` API::

    import aioredis
    from ddtrace import Pin

    myaioredis = aioredis.Aioredis()
    Pin.override(myaioredis, service="myaioredis")
"""
from ...internal.utils.importlib import require_modules


required_modules = ["aioredis"]

with require_modules(required_modules) as missing_modules:
    if not missing_modules:
        from .patch import patch
        from .patch import unpatch

        __all__ = ["patch", "unpatch"]
