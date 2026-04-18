from datetime import datetime, timezone
from typing import Dict, List, Optional

from src.database.models import AuditLog, ResultRecord, ScanRecord, UserRecord, VulnerabilityRecord


class InMemoryDBManager:
    def __init__(self) -> None:
        self._records: List[ScanRecord] = []
        self._vulnerabilities: List[VulnerabilityRecord] = []
        self._results: List[ResultRecord] = []
        self._users: List[UserRecord] = [
            UserRecord(
                id="user-1",
                email="admin@example.com",
                role="admin",
                created_at=datetime.now(timezone.utc),
            )
        ]
        self._audit_logs: List[AuditLog] = []

    def add_scan(self, target: str, risk_score: float, blocked: bool, findings: List[dict]) -> ScanRecord:
        scan_id = f"scan-{len(self._records) + 1}"
        record = ScanRecord(
            id=scan_id,
            target=target,
            risk_score=risk_score,
            blocked=blocked,
            created_at=datetime.now(timezone.utc),
            findings=findings,
        )
        self._records.append(record)

        result_id = f"result-{len(self._results) + 1}"
        self._results.append(
            ResultRecord(
                id=result_id,
                scan_id=scan_id,
                target=target,
                risk_score=risk_score,
                blocked=blocked,
                findings_count=len(findings),
                created_at=record.created_at,
            )
        )

        # Approximate CVSS v3.1 base scores per severity band for reporting output.
        cvss_by_severity = {
            "critical": 9.8,
            "high": 8.0,
            "medium": 5.5,
            "low": 3.1,
        }

        for finding in findings:
            vuln_id = f"vuln-{len(self._vulnerabilities) + 1}"
            severity = finding.get("severity", "low").lower()
            self._vulnerabilities.append(
                VulnerabilityRecord(
                    id=vuln_id,
                    scan_id=scan_id,
                    title=finding.get("title", "Unnamed vulnerability"),
                    description=finding.get("description", ""),
                    severity=severity,
                    vulnerability_type=finding.get("tier", "general"),
                    confidence="high" if severity in {"critical", "high"} else "medium",
                    cwe=f"CWE-{finding.get('id', 'N/A')}",
                    cvss=cvss_by_severity.get(severity, 3.1),
                    parameter=finding.get("payload", "n/a"),
                    poc=finding.get("detection_logic", "n/a"),
                    remediation=finding.get("remediation", "n/a"),
                )
            )

        self._audit_logs.append(
            AuditLog(
                id=f"audit-{len(self._audit_logs) + 1}",
                action="scan_created",
                details={"scan_id": scan_id, "target": target},
                created_at=record.created_at,
            )
        )
        return record

    def list_scans(self) -> List[ScanRecord]:
        return list(self._records)

    def get_scan(self, scan_id: str) -> Optional[ScanRecord]:
        return next((record for record in self._records if record.id == scan_id), None)

    def list_vulnerabilities(self) -> List[VulnerabilityRecord]:
        return list(self._vulnerabilities)

    def list_results(self) -> List[ResultRecord]:
        return list(self._results)

    def initialize_schema(self) -> Dict[str, int]:
        self._audit_logs.append(
            AuditLog(
                id=f"audit-{len(self._audit_logs) + 1}",
                action="schema_initialized",
                details={"status": "ok"},
                created_at=datetime.now(timezone.utc),
            )
        )
        return {
            "scans": len(self._records),
            "vulnerabilities": len(self._vulnerabilities),
            "results": len(self._results),
            "users": len(self._users),
            "audit_logs": len(self._audit_logs),
        }
