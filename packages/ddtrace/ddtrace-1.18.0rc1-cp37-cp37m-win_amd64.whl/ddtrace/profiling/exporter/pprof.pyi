import typing
from typing import Any

from ddtrace.profiling import exporter
from ddtrace.profiling import recorder as recorder
from ddtrace.profiling.collector import _lock
from ddtrace.profiling.collector import memalloc
from ddtrace.profiling.collector import stack_event
from ddtrace.profiling.collector import threading as threading

stdlib_path: Any
platstdlib_path: Any
purelib_path: Any
platlib_path: Any
STDLIB: Any

class Package(typing.TypedDict):
    name: str
    version: str
    kind: typing.Literal["library"]
    paths: typing.List[str]

class pprof_LocationType:
    id: int

class pprof_Mapping:
    filename: int

class pprof_ProfileType:
    id: int
    string_table: typing.Dict[int, str]
    mapping: typing.List[pprof_Mapping]
    def SerializeToString(self) -> bytes: ...

class pprof_FunctionType:
    id: int

HashableStackTraceType: Any

class _PprofConverter:
    def convert_stack_event(
        self,
        thread_id: str,
        thread_native_id: str,
        thread_name: str,
        task_id: str,
        task_name: str,
        local_root_span_id: str,
        span_id: str,
        trace_resource: str,
        trace_type: str,
        frames: HashableStackTraceType,
        nframes: int,
        samples: typing.List[stack_event.StackSampleEvent],
    ) -> None: ...
    def convert_memalloc_event(
        self,
        thread_id: str,
        thread_native_id: str,
        thread_name: str,
        frames: HashableStackTraceType,
        nframes: int,
        events: typing.List[memalloc.MemoryAllocSampleEvent],
    ) -> None: ...
    def convert_memalloc_heap_event(self, event: memalloc.MemoryHeapSampleEvent) -> None: ...
    def convert_lock_acquire_event(
        self,
        lock_name: str,
        thread_id: str,
        thread_name: str,
        task_id: str,
        task_name: str,
        local_root_span_id: str,
        span_id: str,
        trace_resource: str,
        trace_type: str,
        frames: HashableStackTraceType,
        nframes: int,
        events: typing.List[_lock.LockAcquireEvent],
        sampling_ratio: float,
    ) -> None: ...
    def convert_lock_release_event(
        self,
        lock_name: str,
        thread_id: str,
        thread_name: str,
        task_id: str,
        task_name: str,
        local_root_span_id: str,
        span_id: str,
        trace_resource: str,
        trace_type: str,
        frames: HashableStackTraceType,
        nframes: int,
        events: typing.List[_lock.LockReleaseEvent],
        sampling_ratio: float,
    ) -> None: ...
    def convert_stack_exception_event(
        self,
        thread_id: str,
        thread_native_id: str,
        thread_name: str,
        local_root_span_id: str,
        span_id: str,
        trace_resource: str,
        trace_type: str,
        frames: HashableStackTraceType,
        nframes: int,
        exc_type_name: str,
        events: typing.List[stack_event.StackExceptionSampleEvent],
    ) -> None: ...
    def __init__(
        self,
        functions: Any,
        locations: Any,
        string_table: Any,
        last_location_id: Any,
        last_func_id: Any,
        location_values: Any,
    ) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

StackEventGroupKey: Any
LockEventGroupKey: Any
StackExceptionEventGroupKey: Any

class PprofExporter(exporter.Exporter):
    def export(
        self, events: recorder.EventsType, start_time_ns: int, end_time_ns: int
    ) -> typing.Tuple[pprof_ProfileType, typing.List[Package]]: ...
    def __init__(self) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
