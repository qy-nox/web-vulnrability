from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "INFO_DISCLOSURE"
MODULE_TIER = "Information Disclosure"
CHECK_COUNT = 150
PAYLOADS = ["/.git/config", "/backup.zip", "/debug?trace=true"]
DETECTION_PATTERNS = ["debug-endpoint-exposure", "source-leakage", "misconfigured-directory-listing"]
EXPLOITATION_TECHNIQUES = ["error-forcing", "sensitive-file-enumeration", "version-control-discovery"]
REMEDIATION_SUGGESTIONS = ["disable-debug-in-prod", "remove-public-backups", "harden-file-permissions"]
TEST_CASES = ["error-page-response", "static-file-browse", "config-endpoint-access"]


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

