from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List


@dataclass
class ScanRecord:
    id: str
    target: str
    risk_score: float
    blocked: bool
    created_at: datetime
    findings: List[dict]


@dataclass
class VulnerabilityRecord:
    id: str
    scan_id: str
    title: str
    description: str
    severity: str
    vulnerability_type: str
    confidence: str
    cwe: str
    cvss: float
    parameter: str
    poc: str
    remediation: str


@dataclass
class ResultRecord:
    id: str
    scan_id: str
    target: str
    risk_score: float
    blocked: bool
    findings_count: int
    created_at: datetime


@dataclass
class UserRecord:
    id: str
    email: str
    role: str
    created_at: datetime


@dataclass
class AuditLog:
    id: str
    action: str
    details: Dict[str, str]
    created_at: datetime
