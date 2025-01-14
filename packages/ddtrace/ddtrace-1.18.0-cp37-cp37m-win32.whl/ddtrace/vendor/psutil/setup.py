__all__ = ["get_extensions"]

import contextlib
import io
import os
import platform
from setuptools import Extension
import shutil
import sys
import tempfile

POSIX = os.name == "posix"
WINDOWS = os.name == "nt"
LINUX = sys.platform.startswith("linux")
MACOS = sys.platform.startswith("darwin")
OSX = MACOS  # deprecated alias
FREEBSD = sys.platform.startswith("freebsd")
OPENBSD = sys.platform.startswith("openbsd")
NETBSD = sys.platform.startswith("netbsd")
BSD = FREEBSD or OPENBSD or NETBSD
SUNOS = sys.platform.startswith(("sunos", "solaris"))
AIX = sys.platform.startswith("aix")


@contextlib.contextmanager
def silenced_output(stream_name):
    class DummyFile(io.BytesIO):
        # see: https://github.com/giampaolo/psutil/issues/678
        errors = "ignore"

        def write(self, s):
            pass

    orig = getattr(sys, stream_name)
    try:
        setattr(sys, stream_name, DummyFile())
        yield
    finally:
        setattr(sys, stream_name, orig)


def get_extensions():
    macros = [("PSUTIL_VERSION", 567)]
    if POSIX:
        macros.append(("PSUTIL_POSIX", 1))
    if BSD:
        macros.append(("PSUTIL_BSD", 1))

    sources = ["ddtrace/vendor/psutil/_psutil_common.c"]
    if POSIX:
        sources.append("ddtrace/vendor/psutil/_psutil_posix.c")

    if WINDOWS:

        def get_winver():
            win_maj, win_min = sys.getwindowsversion()[0:2]
            return "0x0%s" % ((win_maj * 100) + win_min)

        if sys.getwindowsversion()[0] < 6:
            msg = "this Windows version is too old (< Windows Vista); "
            msg += "psutil 3.4.2 is the latest version which supports Windows "
            msg += "2000, XP and 2003 server"
            raise RuntimeError(msg)

        macros.append(("PSUTIL_WINDOWS", 1))
        macros.extend(
            [
                # be nice to mingw, see:
                # http://www.mingw.org/wiki/Use_more_recent_defined_functions
                ("_WIN32_WINNT", get_winver()),
                ("_AVAIL_WINVER_", get_winver()),
                ("_CRT_SECURE_NO_WARNINGS", None),
                # see: https://github.com/giampaolo/psutil/issues/348
                ("PSAPI_VERSION", 1),
            ]
        )

        sources += [
            "ddtrace/vendor/psutil/_psutil_windows.c",
            "ddtrace/vendor/psutil/arch/windows/process_info.c",
            "ddtrace/vendor/psutil/arch/windows/process_handles.c",
            "ddtrace/vendor/psutil/arch/windows/security.c",
            "ddtrace/vendor/psutil/arch/windows/inet_ntop.c",
            "ddtrace/vendor/psutil/arch/windows/services.c",
            "ddtrace/vendor/psutil/arch/windows/global.c",
            "ddtrace/vendor/psutil/arch/windows/wmi.c",
        ]
        ext = Extension(
            "ddtrace.vendor.psutil._psutil_windows",
            sources=sources,
            define_macros=macros,
            libraries=[
                "psapi",
                "kernel32",
                "advapi32",
                "shell32",
                "netapi32",
                "wtsapi32",
                "ws2_32",
                "PowrProf",
                "pdh",
            ],
            # extra_compile_args=["/Z7"],
            # extra_link_args=["/DEBUG"]
        )

    elif MACOS:
        macros.append(("PSUTIL_OSX", 1))
        sources += [
            "ddtrace/vendor/psutil/_psutil_osx.c",
            "ddtrace/vendor/psutil/arch/osx/process_info.c",
        ]
        ext = Extension(
            "ddtrace.vendor.psutil._psutil_osx",
            sources=sources,
            define_macros=macros,
            extra_link_args=["-framework", "CoreFoundation", "-framework", "IOKit"],
        )

    elif FREEBSD:
        macros.append(("PSUTIL_FREEBSD", 1))
        sources += [
            "ddtrace/vendor/psutil/_psutil_bsd.c",
            "ddtrace/vendor/psutil/arch/freebsd/specific.c",
            "ddtrace/vendor/psutil/arch/freebsd/sys_socks.c",
            "ddtrace/vendor/psutil/arch/freebsd/proc_socks.c",
        ]
        ext = Extension(
            "ddtrace.vendor.psutil._psutil_bsd", sources=sources, define_macros=macros, libraries=["devstat"],
        )

    elif OPENBSD:
        macros.append(("PSUTIL_OPENBSD", 1))
        ext = Extension(
            "ddtrace.vendor.psutil._psutil_bsd",
            sources=sources + ["ddtrace/vendor/psutil/_psutil_bsd.c", "ddtrace/vendor/psutil/arch/openbsd/specific.c"],
            define_macros=macros,
            libraries=["kvm"],
        )

    elif NETBSD:
        macros.append(("PSUTIL_NETBSD", 1))
        sources += [
            "ddtrace/vendor/psutil/_psutil_bsd.c",
            "ddtrace/vendor/psutil/arch/netbsd/specific.c",
            "ddtrace/vendor/psutil/arch/netbsd/socks.c",
        ]
        ext = Extension("ddtrace.vendor.psutil._psutil_bsd", sources=sources, define_macros=macros, libraries=["kvm"],)

    elif LINUX:

        def get_ethtool_macro():
            # see: https://github.com/giampaolo/ddtrace/vendor/psutil/issues/659
            from distutils.unixccompiler import UnixCCompiler
            from distutils.errors import CompileError

            with tempfile.NamedTemporaryFile(suffix=".c", delete=False, mode="wt") as f:
                f.write("#include <linux/ethtool.h>")

            output_dir = tempfile.mkdtemp()
            try:
                compiler = UnixCCompiler()
                # https://github.com/giampaolo/ddtrace/vendor/psutil/pull/1568
                if os.getenv("CC"):
                    compiler.set_executable("compiler_so", os.getenv("CC"))
                with silenced_output("stderr"):
                    with silenced_output("stdout"):
                        compiler.compile([f.name], output_dir=output_dir)
            except CompileError:
                return ("PSUTIL_ETHTOOL_MISSING_TYPES", 1)
            else:
                return None
            finally:
                os.remove(f.name)
                shutil.rmtree(output_dir)

        macros.append(("PSUTIL_LINUX", 1))
        ETHTOOL_MACRO = get_ethtool_macro()
        if ETHTOOL_MACRO is not None:
            macros.append(ETHTOOL_MACRO)
        ext = Extension(
            "ddtrace.vendor.psutil._psutil_linux",
            sources=sources + ["ddtrace/vendor/psutil/_psutil_linux.c"],
            define_macros=macros,
        )

    elif SUNOS:
        macros.append(("PSUTIL_SUNOS", 1))
        sources += [
            "ddtrace/vendor/psutil/_psutil_sunos.c",
            "ddtrace/vendor/psutil/arch/solaris/v10/ifaddrs.c",
            "ddtrace/vendor/psutil/arch/solaris/environ.c",
        ]
        ext = Extension(
            "ddtrace.vendor.psutil._psutil_sunos",
            sources=sources,
            define_macros=macros,
            libraries=["kstat", "nsl", "socket"],
        )

    elif AIX:
        macros.append(("PSUTIL_AIX", 1))
        sources += [
            "ddtrace/vendor/psutil/_psutil_aix.c",
            "ddtrace/vendor/psutil/arch/aix/net_connections.c",
            "ddtrace/vendor/psutil/arch/aix/common.c",
            "ddtrace/vendor/psutil/arch/aix/ifaddrs.c",
        ]
        ext = Extension(
            "ddtrace.vendor.psutil._psutil_aix", sources=sources, libraries=["perfstat"], define_macros=macros,
        )
    else:
        raise RuntimeError("platform %s is not supported" % sys.platform)

    if POSIX:
        posix_extension = Extension("ddtrace.vendor.psutil._psutil_posix", define_macros=macros, sources=sources)
        if SUNOS:
            posix_extension.libraries.append("socket")
            if platform.release() == "5.10":
                posix_extension.sources.append("ddtrace/vendor/psutil/arch/solaris/v10/ifaddrs.c")
                posix_extension.define_macros.append(("PSUTIL_SUNOS10", 1))
        elif AIX:
            posix_extension.sources.append("ddtrace/vendor/psutil/arch/aix/ifaddrs.c")

        return [ext, posix_extension]
    else:
        return [ext]
