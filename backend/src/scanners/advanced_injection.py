from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "ADVANCED_INJECTION"
MODULE_TIER = "Advanced Injection"
CHECK_COUNT = 200
PAYLOADS = ["'||1=1--", "${jndi:ldap://example}", "{{7*7}}"]
DETECTION_PATTERNS = ["nosql-injection", "command-injection", "template-injection"]
EXPLOITATION_TECHNIQUES = ["polyglot-payload", "encoding-bypass", "context-breaking"]
REMEDIATION_SUGGESTIONS = ["parameterize-inputs", "sanitize-template-context", "restrict-shell-exec"]
TEST_CASES = ["json-body-injection", "query-parameter-injection", "header-injection"]


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

