from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "SSRF"
MODULE_TIER = "Server-Side Request Forgery"
CHECK_COUNT = 120
PAYLOADS = ["http://169.254.169.254/latest/meta-data/", "gopher://127.0.0.1:6379", "http://localhost/admin"]
DETECTION_PATTERNS = ["metadata-endpoint-access", "internal-network-reachability", "redirect-following-abuse"]
EXPLOITATION_TECHNIQUES = ["dns-rebinding", "protocol-smuggling", "blind-ssrf-timing"]
REMEDIATION_SUGGESTIONS = ["egress-filtering", "allowlist-outbound-hosts", "disable-unsafe-protocols"]
TEST_CASES = ["url-fetch-endpoint", "webhook-delivery", "pdf-render-service"]


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

