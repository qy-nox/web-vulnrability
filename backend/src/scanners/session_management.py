from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "SESSION_MANAGEMENT"
MODULE_TIER = "Session Management"
CHECK_COUNT = 120
PAYLOADS = ["predictable-session-id", "missing-httpOnly", "session-fixation-cookie"]
DETECTION_PATTERNS = ["cookie-security-misconfig", "session-fixation", "session-timeout-weakness"]
EXPLOITATION_TECHNIQUES = ["session-hijacking", "token-reuse", "cookie-tampering"]
REMEDIATION_SUGGESTIONS = ["regenerate-session-after-login", "set-secure-cookie-flags", "shorten-session-lifetime"]
TEST_CASES = ["login-session-rotation", "remember-me-cookie", "logout-invalidates-token"]


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

