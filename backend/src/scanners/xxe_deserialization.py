from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "XXE_DESERIALIZATION"
MODULE_TIER = "XXE/Deserialization"
CHECK_COUNT = 220
PAYLOADS = ["<!DOCTYPE x [<!ENTITY xxe SYSTEM 'file:///etc/passwd'>]>", "pickle-rce-object", "ysoserial-chain"]
DETECTION_PATTERNS = ["external-entity-processing", "unsafe-object-deserialization", "xml-parser-misuse"]
EXPLOITATION_TECHNIQUES = ["external-dtd-injection", "gadget-chain-execution", "billion-laughs"]
REMEDIATION_SUGGESTIONS = ["disable-external-entities", "use-safe-deserializers", "validate-serialized-input"]
TEST_CASES = ["xml-upload-parser", "soap-endpoint", "serialized-session-store"]


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
