from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "CRYPTOGRAPHY"
MODULE_TIER = "Cryptography"
CHECK_COUNT = 130
PAYLOADS = ["weak-cipher-suite", "iv-reuse-sample", "hardcoded-key-pattern"]
DETECTION_PATTERNS = ["weak-cipher-detection", "insecure-randomness", "certificate-validation-issue"]
EXPLOITATION_TECHNIQUES = ["padding-oracle", "key-reuse-analysis", "downgrade-negotiation"]
REMEDIATION_SUGGESTIONS = ["use-modern-ciphers", "rotate-keys", "enforce-tls-1.2-plus"]
TEST_CASES = ["tls-handshake-analysis", "jwt-signing-key-audit", "encryption-config-review"]


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

