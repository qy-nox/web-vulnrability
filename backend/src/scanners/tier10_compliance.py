from typing import Dict, List

TIER_NAME = "Tier 10: Compliance & Regulatory"
TIER_CODE = "TIER10_COMPLIANCE"
CHECK_COUNT = 90
FAMILIES = ['hipaa', 'gdpr', 'pci-dss', 'owasp-top-10', 'cwe-cve-mapping']


def build_checks() -> List[Dict[str, str]]:
    checks: List[Dict[str, str]] = []
    for index in range(1, CHECK_COUNT + 1):
        family = FAMILIES[(index - 1) % len(FAMILIES)]
        checks.append({
            "id": f"{TIER_CODE}-{index:03d}",
            "tier": TIER_NAME,
            "family": family,
            "name": f"{family} check {index}",
            "severity": ["critical", "high", "medium", "low"][index % 4],
            "owasp": f"A{(index % 10) + 1}",
        })
    return checks
