from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "SERVER_SIDE_RENDERING"
MODULE_TIER = "Server-Side Rendering"
CHECK_COUNT = 100
PAYLOADS = ["{{7*7}}", "${7*7}", "#{7*7}"]
DETECTION_PATTERNS = ["ssti-vector", "expression-language-injection", "response-smuggling-signal"]
EXPLOITATION_TECHNIQUES = ["template-context-breakout", "header-desync", "render-pipeline-abuse"]
REMEDIATION_SUGGESTIONS = ["disable-unsafe-template-eval", "strict-header-parsing", "sandbox-render-context"]
TEST_CASES = ["server-rendered-page", "email-template-render", "pdf-template-render"]


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

