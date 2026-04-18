from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class ScanRecord:
    target: str
    risk_score: float
    blocked: bool
    created_at: datetime
    findings: List[dict]
