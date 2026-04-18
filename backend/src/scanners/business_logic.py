from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "BUSINESS_LOGIC"
MODULE_TIER = "Business Logic"
CHECK_COUNT = 150
PAYLOADS = ["negative-price", "coupon-reuse", "state-transition-skip"]
DETECTION_PATTERNS = ["workflow-bypass", "price-manipulation", "idor-sequence"]
EXPLOITATION_TECHNIQUES = ["race-condition", "parameter-tampering", "order-of-operations-abuse"]
REMEDIATION_SUGGESTIONS = ["server-side-price-validation", "enforce-state-machine", "resource-owner-checks"]
TEST_CASES = ["checkout-flow", "refund-flow", "coupon-redemption"]


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

