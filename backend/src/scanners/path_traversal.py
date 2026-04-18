from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "PATH_TRAVERSAL"
MODULE_TIER = "Path Traversal"
CHECK_COUNT = 100
PAYLOADS = ["../../../../etc/passwd", "..%2f..%2fwindows/win.ini", "..%252f..%252fapp/config"]
DETECTION_PATTERNS = ["directory-traversal", "double-encoding-bypass", "null-byte-path-bypass"]
EXPLOITATION_TECHNIQUES = ["backtracking", "unicode-encoding-evasion", "path-normalization-confusion"]
REMEDIATION_SUGGESTIONS = ["normalize-and-validate-paths", "use-allowlisted-filenames", "block-relative-path-input"]
TEST_CASES = ["download-endpoint", "template-loader", "archive-extract-endpoint"]


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

