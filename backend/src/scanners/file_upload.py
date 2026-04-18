from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "FILE_UPLOAD"
MODULE_TIER = "File Upload"
CHECK_COUNT = 120
PAYLOADS = ["polyglot-jpg-php", "double-extension.php.jpg", "svg-script-upload"]
DETECTION_PATTERNS = ["mime-type-bypass", "extension-filter-bypass", "upload-path-traversal"]
EXPLOITATION_TECHNIQUES = ["content-type-confusion", "filename-poisoning", "webshell-drop"]
REMEDIATION_SUGGESTIONS = ["strict-file-type-validation", "store-outside-web-root", "scan-uploads-with-av"]
TEST_CASES = ["avatar-upload", "document-upload", "bulk-import-upload"]


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

