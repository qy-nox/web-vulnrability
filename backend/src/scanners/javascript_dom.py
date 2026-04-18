from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "JAVASCRIPT_DOM"
MODULE_TIER = "JavaScript/DOM"
CHECK_COUNT = 140
PAYLOADS = ["<img src=x onerror=alert(1)>", "__proto__.polluted=true", "dom-clobber-id"]
DETECTION_PATTERNS = ["dom-xss-vector", "prototype-pollution", "unsafe-dom-sink"]
EXPLOITATION_TECHNIQUES = ["event-handler-injection", "dom-clobbering", "client-template-abuse"]
REMEDIATION_SUGGESTIONS = ["sanitize-dom-input", "use-safe-dom-apis", "freeze-critical-prototypes"]
TEST_CASES = ["single-page-app-router", "comment-renderer", "markdown-preview"]


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

