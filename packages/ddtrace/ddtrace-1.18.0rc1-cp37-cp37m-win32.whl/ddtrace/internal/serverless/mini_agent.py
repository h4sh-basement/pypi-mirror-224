import os
from subprocess import Popen
import sys

from ..compat import PYTHON_VERSION_INFO
from ..logger import get_logger
from ..serverless import in_azure_function_consumption_plan
from ..serverless import in_gcp_function


log = get_logger(__name__)


def maybe_start_serverless_mini_agent():
    if not (in_gcp_function() or in_azure_function_consumption_plan()):
        return

    if sys.platform != "win32" and sys.platform != "linux":
        log.error("Serverless Mini Agent is only supported on Windows and Linux.")
        return

    try:
        rust_binary_path = get_rust_binary_path()

        log.debug("Trying to spawn the Serverless Mini Agent at path: %s", rust_binary_path)
        Popen(rust_binary_path)
    except Exception as e:
        log.error("Error spawning Serverless Mini Agent process: %s", repr(e))


def get_rust_binary_path():
    rust_binary_path = os.getenv("DD_MINI_AGENT_PATH")

    if rust_binary_path is not None:
        return rust_binary_path

    if in_gcp_function():
        rust_binary_path = (
            "/layers/google.python.pip/pip/lib/python{}.{}/site-packages/"
            "datadog-serverless-agent-linux-amd64/datadog-serverless-trace-mini-agent"
        ).format(PYTHON_VERSION_INFO[0], PYTHON_VERSION_INFO[1])
    else:
        rust_binary_path = (
            "/home/site/wwwroot/.python_packages/lib/site-packages/"
            "datadog-serverless-agent-linux-amd64/datadog-serverless-trace-mini-agent"
        )

    return rust_binary_path
