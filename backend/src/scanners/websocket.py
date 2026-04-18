from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "WEBSOCKET"
MODULE_TIER = "WebSocket"
CHECK_COUNT = 100
PAYLOADS = ["ws-origin-forgery", "oversized-frame", "auth-token-missing"]
DETECTION_PATTERNS = ["origin-validation-bypass", "message-integrity-weakness", "websocket-auth-bypass"]
EXPLOITATION_TECHNIQUES = ["cross-site-websocket-hijack", "frame-manipulation", "compression-side-channel"]
REMEDIATION_SUGGESTIONS = ["validate-origin", "require-auth-on-connect", "limit-frame-size"]
TEST_CASES = ["ws-chat-channel", "ws-notification-channel", "ws-admin-channel"]


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
