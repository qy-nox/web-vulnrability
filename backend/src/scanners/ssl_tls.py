from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "SSL_TLS"
MODULE_TIER = "SSL/TLS"
CHECK_COUNT = 130
PAYLOADS = ["tls1.0-handshake", "weak-certificate-signature", "insecure-cipher-suite-offer"]
DETECTION_PATTERNS = ["protocol-downgrade-risk", "certificate-validation-weakness", "weak-cipher-negotiation"]
EXPLOITATION_TECHNIQUES = ["ssl-stripping", "cipher-downgrade", "certificate-spoofing"]
REMEDIATION_SUGGESTIONS = ["disable-legacy-protocols", "enforce-strong-ciphers", "automate-certificate-rotation"]
TEST_CASES = ["https-endpoint-scan", "certificate-chain-validation", "tls-configuration-review"]


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
