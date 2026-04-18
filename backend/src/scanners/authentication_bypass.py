from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "AUTH_BYPASS"
MODULE_TIER = "Authentication Bypass"
CHECK_COUNT = 150
PAYLOADS = ["none-alg-jwt", "otp-replay-token", "session-fixation-cookie"]
DETECTION_PATTERNS = ["jwt-validation-weakness", "mfa-bypass", "session-prediction"]
EXPLOITATION_TECHNIQUES = ["token-forgery", "auth-flow-race", "credential-stuffing-pattern"]
REMEDIATION_SUGGESTIONS = ["enforce-token-verification", "harden-mfa", "rotate-session-identifiers"]
TEST_CASES = ["oauth-code-flow", "saml-assertion-validation", "password-reset-flow"]


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

