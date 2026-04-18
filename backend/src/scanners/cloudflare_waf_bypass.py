from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "CLOUDFLARE_WAF_BYPASS"
MODULE_TIER = "CloudFlare/WAF Bypass"
CHECK_COUNT = 150
PAYLOADS = ["cf-ray-spoof", "x-origin-bypass", "header-case-rotation"]
DETECTION_PATTERNS = ["challenge-bypass", "waf-signature-evasion", "origin-discovery"]
EXPLOITATION_TECHNIQUES = ["header-smuggling", "request-normalization-evasion", "origin-probing"]
REMEDIATION_SUGGESTIONS = ["restrict-origin-access", "normalize-requests", "enable-bot-management"]
TEST_CASES = ["cloudflare-challenge", "generic-waf-bypass", "origin-ip-exposure"]


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
