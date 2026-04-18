from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "DEPENDENCIES"
MODULE_TIER = "Dependency Security"
CHECK_COUNT = 200
PAYLOADS = ["known-cve-package", "typosquat-package-name", "dependency-confusion-scope"]
DETECTION_PATTERNS = ["vulnerable-version-detection", "supply-chain-risk", "transitive-risk"]
EXPLOITATION_TECHNIQUES = ["malicious-package-substitution", "registry-priority-abuse", "lockfile-poisoning"]
REMEDIATION_SUGGESTIONS = ["pin-and-update-dependencies", "verify-package-signatures", "use-private-registry-controls"]
TEST_CASES = ["pip-lock-scan", "npm-lock-scan", "maven-dependency-tree"]


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

