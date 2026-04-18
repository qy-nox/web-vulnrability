from datetime import datetime
from typing import List

from src.database.models import ScanRecord


class InMemoryDBManager:
    def __init__(self) -> None:
        self._records: List[ScanRecord] = []

    def add_scan(self, target: str, risk_score: float, blocked: bool, findings: List[dict]) -> ScanRecord:
        record = ScanRecord(
            target=target,
            risk_score=risk_score,
            blocked=blocked,
            created_at=datetime.utcnow(),
            findings=findings,
        )
        self._records.append(record)
        return record

    def list_scans(self) -> List[ScanRecord]:
        return list(self._records)
