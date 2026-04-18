from typing import Dict

from src.reporting.compliance_reports import map_to_compliance


class ReportGenerator:
    def generate_json_report(self, scan_output: Dict[str, object]) -> Dict[str, object]:
        findings_count = len(scan_output.get("findings", []))
        return {
            "executive_summary": {
                "target": scan_output.get("target"),
                "risk_score": scan_output.get("risk_score"),
                "blocked": scan_output.get("blocked"),
            },
            "technical_details": scan_output,
            "compliance": map_to_compliance(findings_count),
        }
