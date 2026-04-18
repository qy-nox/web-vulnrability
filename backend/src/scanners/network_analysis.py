from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "NETWORK_ANALYSIS"
MODULE_TIER = "Network Analysis"
CHECK_COUNT = 120
PAYLOADS = ["port-sweep-sequence", "dns-amplification-probe", "tcp-fragment-pattern"]
DETECTION_PATTERNS = ["open-service-exposure", "anomalous-network-flow", "internal-port-reachability"]
EXPLOITATION_TECHNIQUES = ["service-fingerprinting", "timing-analysis", "protocol-downgrade"]
REMEDIATION_SUGGESTIONS = ["close-unused-ports", "segment-internal-network", "monitor-anomalous-traffic"]
TEST_CASES = ["edge-firewall-scan", "internal-segment-scan", "service-banner-scan"]


def build_checks() -> List[Dict[str, str]]:
    return build_checks_for_module(
        MODULE_CODE,
        MODULE_TIER,
        CHECK_COUNT,
        PAYLOADS,
        DETECTION_PATTERNS,
        EXPLOITATION_TECHNIQUES,
        REMEDIATION_SUGGESTIONS,
        TEST_CASES,
    )

