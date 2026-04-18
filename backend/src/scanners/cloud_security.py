from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "CLOUD_SECURITY"
MODULE_TIER = "Cloud Security"
CHECK_COUNT = 200
PAYLOADS = ["s3-public-list", "metadata-access", "iam-policy-overly-permissive"]
DETECTION_PATTERNS = ["storage-misconfiguration", "metadata-exposure", "iam-privilege-escalation"]
EXPLOITATION_TECHNIQUES = ["bucket-enumeration", "instance-role-abuse", "policy-chaining"]
REMEDIATION_SUGGESTIONS = ["least-privilege-iam", "private-storage-by-default", "restrict-metadata-endpoints"]
TEST_CASES = ["aws-s3-config", "azure-storage-config", "gcp-bucket-config"]


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

