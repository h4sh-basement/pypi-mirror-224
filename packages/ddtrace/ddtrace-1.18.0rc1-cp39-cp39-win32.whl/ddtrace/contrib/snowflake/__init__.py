"""
The snowflake integration instruments the ``snowflake-connector-python`` library to trace Snowflake queries.

Note that this integration is in beta.

Enabling
~~~~~~~~

The integration is not enabled automatically when using
:ref:`ddtrace-run<ddtracerun>` or :func:`patch_all()<ddtrace.patch_all>`.

Use :func:`patch()<ddtrace.patch>` to manually enable the integration::

    from ddtrace import patch, patch_all
    patch(snowflake=True)
    patch_all(snowflake=True)

or the ``DD_TRACE_SNOWFLAKE_ENABLED=true`` to enable it with ``ddtrace-run``.


Global Configuration
~~~~~~~~~~~~~~~~~~~~

.. py:data:: ddtrace.config.snowflake["service"]

   The service name reported by default for snowflake spans.

   This option can also be set with the ``DD_SNOWFLAKE_SERVICE`` environment
   variable.

   Default: ``"snowflake"``

.. py:data:: ddtrace.config.snowflake["trace_fetch_methods"]

   Whether or not to trace fetch methods.

   Can also configured via the ``DD_SNOWFLAKE_TRACE_FETCH_METHODS`` environment variable.

   Default: ``False``


Instance Configuration
~~~~~~~~~~~~~~~~~~~~~~

To configure the integration on an per-connection basis use the
``Pin`` API::

    from ddtrace import Pin
    from snowflake.connector import connect

    # This will report a span with the default settings
    conn = connect(user="alice", password="b0b", account="dev")

    # Use a pin to override the service name for this connection.
    Pin.override(conn, service="snowflake-dev")


    cursor = conn.cursor()
    cursor.execute("SELECT current_version()")
"""
from ...internal.utils.importlib import require_modules


required_modules = ["snowflake.connector"]

with require_modules(required_modules) as missing_modules:
    if not missing_modules:
        from .patch import patch
        from .patch import unpatch

        __all__ = ["patch", "unpatch"]
