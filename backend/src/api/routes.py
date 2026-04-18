from typing import List

from fastapi import APIRouter
from pydantic import BaseModel, Field, HttpUrl

from src.core.advanced_scanner import SCANNER
from src.database.db_manager import InMemoryDBManager
from src.reporting.report_generator import ReportGenerator
from src.utils.config import CONFIG

router = APIRouter(prefix="/api/v1")
DB = InMemoryDBManager()
REPORTER = ReportGenerator()


class ScanRequest(BaseModel):
    url: HttpUrl


class BatchScanRequest(BaseModel):
    urls: List[HttpUrl] = Field(min_length=1, max_length=CONFIG.max_batch_targets)


@router.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "advanced-web-vulnerability-system"}


@router.get("/checks/summary")
def checks_summary() -> dict:
    return SCANNER.checks_summary()


@router.post("/scan")
def scan(request: ScanRequest) -> dict:
    result = SCANNER.scan_target(str(request.url))
    DB.add_scan(result.target, result.risk_score, result.blocked, result.findings)
    return REPORTER.generate_json_report(result.__dict__)


@router.post("/scan/batch")
def scan_batch(request: BatchScanRequest) -> dict:
    outputs = []
    for url in request.urls:
        result = SCANNER.scan_target(str(url))
        outputs.append(REPORTER.generate_json_report(result.__dict__))
    return {"count": len(outputs), "results": outputs}


@router.get("/scans")
def list_scans() -> dict:
    records = DB.list_scans()
    return {
        "count": len(records),
        "items": [
            {
                "target": r.target,
                "risk_score": r.risk_score,
                "blocked": r.blocked,
                "created_at": r.created_at.isoformat() + "Z",
            }
            for r in records
        ],
    }
