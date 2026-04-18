from typing import Dict


def map_to_compliance(findings_count: int) -> Dict[str, str]:
    return {
        "HIPAA": "review" if findings_count else "pass",
        "GDPR": "review" if findings_count else "pass",
        "PCI-DSS": "review" if findings_count else "pass",
        "ISO 27001": "review" if findings_count else "pass",
    }
