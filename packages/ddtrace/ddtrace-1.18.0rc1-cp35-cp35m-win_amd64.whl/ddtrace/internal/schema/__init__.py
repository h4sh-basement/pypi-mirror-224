import logging
import os

from ddtrace.internal.utils.formats import asbool

from .span_attribute_schema import SpanDirection
from .span_attribute_schema import _DEFAULT_SPAN_SERVICE_NAMES
from .span_attribute_schema import _SPAN_ATTRIBUTE_TO_FUNCTION


log = logging.getLogger(__name__)


# Span attribute schema
def _validate_schema(version):
    error_message = (
        "You have specified an invalid span attribute schema version: '{}'.".format(version),
        "Valid options are: {}. You can change the specified value by updating".format(
            _SPAN_ATTRIBUTE_TO_FUNCTION.keys()
        ),
        "the value exported in the 'DD_TRACE_SPAN_ATTRIBUTE_SCHEMA' environment variable.",
    )

    if version not in _SPAN_ATTRIBUTE_TO_FUNCTION.keys():
        log.warning(" ".join(error_message))
        return False

    return True


def _get_schema_version():
    version = os.getenv("DD_TRACE_SPAN_ATTRIBUTE_SCHEMA", default="v0")
    if not _validate_schema(version):
        version = "v0"
    return version


SCHEMA_VERSION = _get_schema_version()
_remove_client_service_names = asbool(os.getenv("DD_TRACE_REMOVE_INTEGRATION_SERVICE_NAMES_ENABLED", default=False))
_service_name_schema_version = "v0" if SCHEMA_VERSION == "v0" and not _remove_client_service_names else "v1"

DEFAULT_SPAN_SERVICE_NAME = _DEFAULT_SPAN_SERVICE_NAMES[_service_name_schema_version]
schematize_cache_operation = _SPAN_ATTRIBUTE_TO_FUNCTION[SCHEMA_VERSION]["cache_operation"]
schematize_cloud_api_operation = _SPAN_ATTRIBUTE_TO_FUNCTION[SCHEMA_VERSION]["cloud_api_operation"]
schematize_cloud_faas_operation = _SPAN_ATTRIBUTE_TO_FUNCTION[SCHEMA_VERSION]["cloud_faas_operation"]
schematize_cloud_messaging_operation = _SPAN_ATTRIBUTE_TO_FUNCTION[SCHEMA_VERSION]["cloud_messaging_operation"]
schematize_database_operation = _SPAN_ATTRIBUTE_TO_FUNCTION[SCHEMA_VERSION]["database_operation"]
schematize_messaging_operation = _SPAN_ATTRIBUTE_TO_FUNCTION[SCHEMA_VERSION]["messaging_operation"]
schematize_service_name = _SPAN_ATTRIBUTE_TO_FUNCTION[_service_name_schema_version]["service_name"]
schematize_url_operation = _SPAN_ATTRIBUTE_TO_FUNCTION[SCHEMA_VERSION]["url_operation"]

__all__ = [
    "DEFAULT_SPAN_SERVICE_NAME",
    "SCHEMA_VERSION",
    "SpanDirection",
    "schematize_cache_operation",
    "schematize_cloud_api_operation",
    "schematize_cloud_faas_operation",
    "schematize_cloud_messaging_operation",
    "schematize_database_operation",
    "schematize_messaging_operation",
    "schematize_service_name",
    "schematize_url_operation",
]
