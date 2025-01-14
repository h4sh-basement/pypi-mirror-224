from ddtrace.appsec.iast import oce
from ddtrace.appsec.iast._taint_tracking import taint_ranges_as_evidence_info
from ddtrace.appsec.iast.constants import EVIDENCE_CMDI
from ddtrace.appsec.iast.constants import VULN_CMDI
from ddtrace.appsec.iast.taint_sinks._base import VulnerabilityBase


@oce.register
class CommandInjection(VulnerabilityBase):
    vulnerability_type = VULN_CMDI
    evidence_type = EVIDENCE_CMDI

    @classmethod
    def report(cls, evidence_value=None, sources=None):
        if isinstance(evidence_value, (str, bytes, bytearray)):
            evidence_value, sources = taint_ranges_as_evidence_info(evidence_value)
        super(CommandInjection, cls).report(evidence_value=evidence_value, sources=sources)
