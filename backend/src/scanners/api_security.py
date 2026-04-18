from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "API_SECURITY"
MODULE_TIER = "API Security"
CHECK_COUNT = 180
PAYLOADS = ["graphql-introspection", "rate-limit-burst", "auth-header-confusion"]
DETECTION_PATTERNS = ["schema-enumeration", "api-auth-bypass", "pagination-abuse"]
EXPLOITATION_TECHNIQUES = ["depth-limit-evasion", "parameter-pollution", "token-replay"]
REMEDIATION_SUGGESTIONS = ["disable-prod-introspection", "enforce-rate-limits", "strict-authz-checks"]
TEST_CASES = ["graphql-endpoint", "rest-endpoint", "openapi-discovery"]


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

