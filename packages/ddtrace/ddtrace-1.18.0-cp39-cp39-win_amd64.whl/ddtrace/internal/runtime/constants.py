GC_COUNT_GEN0 = "runtime.python.gc.count.gen0"
GC_COUNT_GEN1 = "runtime.python.gc.count.gen1"
GC_COUNT_GEN2 = "runtime.python.gc.count.gen2"

THREAD_COUNT = "runtime.python.thread_count"
MEM_RSS = "runtime.python.mem.rss"
# `runtime.python.cpu.time.sys` metric is used to auto-enable runtime metrics dashboards in DD backend
CPU_TIME_SYS = "runtime.python.cpu.time.sys"
CPU_TIME_USER = "runtime.python.cpu.time.user"
CPU_PERCENT = "runtime.python.cpu.percent"
CTX_SWITCH_VOLUNTARY = "runtime.python.cpu.ctx_switch.voluntary"
CTX_SWITCH_INVOLUNTARY = "runtime.python.cpu.ctx_switch.involuntary"

GC_RUNTIME_METRICS = set([GC_COUNT_GEN0, GC_COUNT_GEN1, GC_COUNT_GEN2])

PSUTIL_RUNTIME_METRICS = set(
    [THREAD_COUNT, MEM_RSS, CTX_SWITCH_VOLUNTARY, CTX_SWITCH_INVOLUNTARY, CPU_TIME_SYS, CPU_TIME_USER, CPU_PERCENT]
)

DEFAULT_RUNTIME_METRICS = GC_RUNTIME_METRICS | PSUTIL_RUNTIME_METRICS

SERVICE = "service"
ENV = "env"
LANG_INTERPRETER = "lang_interpreter"
LANG_VERSION = "lang_version"
LANG = "lang"
TRACER_VERSION = "tracer_version"
