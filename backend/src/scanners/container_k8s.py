from typing import Dict, List

from src.scanners.module_checks import build_checks_for_module

MODULE_CODE = "CONTAINER_K8S"
MODULE_TIER = "Container/Kubernetes"
CHECK_COUNT = 150
PAYLOADS = ["privileged-pod", "hostpath-mount", "serviceaccount-token-abuse"]
DETECTION_PATTERNS = ["rbac-misconfiguration", "etcd-exposure", "container-escape-vector"]
EXPLOITATION_TECHNIQUES = ["namespace-breakout", "api-server-abuse", "runtime-privilege-escalation"]
REMEDIATION_SUGGESTIONS = ["enforce-pod-security", "restrict-service-accounts", "harden-k8s-network-policies"]
TEST_CASES = ["cluster-rbac-audit", "image-policy-validation", "pod-security-standards"]


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
