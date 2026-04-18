from typing import Dict, List

TIER_NAME = "Tier 6: Client-Side Advanced"
TIER_CODE = "TIER6_CLIENT_SIDE"
CHECK_COUNT = 100
FAMILIES = ['js-deobfuscation', 'dom-manipulation', 'service-worker-security', 'websocket-security', 'webrtc-ip-leak']


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
