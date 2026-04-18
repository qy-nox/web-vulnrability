from typing import Dict, List


def build_checks_for_module(
    module_code: str,
    module_tier: str,
    check_count: int,
    payloads: List[str],
    detection_patterns: List[str],
    exploitation_techniques: List[str],
    remediation_suggestions: List[str],
    test_cases: List[str],
) -> List[Dict[str, str]]:
    checks: List[Dict[str, str]] = []
    severities = ["critical", "high", "medium", "low"]
    for index in range(1, check_count + 1):
        payload = payloads[(index - 1) % len(payloads)]
        detection = detection_patterns[(index - 1) % len(detection_patterns)]
        exploit = exploitation_techniques[(index - 1) % len(exploitation_techniques)]
        remediation = remediation_suggestions[(index - 1) % len(remediation_suggestions)]
        test_case = test_cases[(index - 1) % len(test_cases)]

        checks.append(
            {
                "id": f"{module_code}-{index:03d}",
                "tier": module_tier,
                "family": detection,
                "name": f"{module_tier} check {index}",
                "severity": severities[index % len(severities)],
                "owasp": f"A{(index % 10) + 1}",
                "payload": payload,
                "detection_logic": detection,
                "exploitation_technique": exploit,
                "remediation": remediation,
                "test_case": test_case,
            }
        )
    return checks
