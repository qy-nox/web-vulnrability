from typing import List

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field, HttpUrl

from datetime import timezone

from src.core.advanced_scanner import SCANNER
from src.database.db_manager import InMemoryDBManager
from src.reporting.report_generator import ReportGenerator
from src.utils.config import CONFIG

router = APIRouter()
DB = InMemoryDBManager()
REPORTER = ReportGenerator()
DB.initialize_schema()
ALLOWED_SEVERITIES = {"critical", "high", "medium", "low"}


def _utc_iso(dt) -> str:
    return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


class ScanRequest(BaseModel):
    url: HttpUrl


class BatchScanRequest(BaseModel):
    urls: List[HttpUrl] = Field(min_length=1, max_length=CONFIG.max_batch_targets)


@router.get("/api/v1/health")
@router.get("/api/health")
def health() -> dict:
    return {"status": "ok", "service": "advanced-web-vulnerability-system"}


@router.get("/api/v1/checks/summary")
@router.get("/api/checks/summary")
def checks_summary() -> dict:
    return SCANNER.checks_summary()


def _run_scan(url: str) -> dict:
    result = SCANNER.scan_target(url)
    record = DB.add_scan(result.target, result.risk_score, result.blocked, result.findings)
    report = REPORTER.generate_json_report(result.__dict__)
    return {"scan_id": record.id, "status": "completed", "report": report}


@router.post("/api/v1/scan")
@router.post("/api/scan")
def scan(request: ScanRequest) -> dict:
    return _run_scan(str(request.url))


@router.post("/api/v1/scan/batch")
def scan_batch(request: BatchScanRequest) -> dict:
    outputs: List[dict] = []
    for url in request.urls:
        outputs.append(_run_scan(str(url)))
    return {"count": len(outputs), "results": outputs}


@router.get("/api/v1/scans")
def list_scans() -> dict:
    records = DB.list_scans()
    return {
        "count": len(records),
        "items": [
            {
                "id": r.id,
                "target": r.target,
                "risk_score": r.risk_score,
                "blocked": r.blocked,
                "created_at": _utc_iso(r.created_at),
            }
            for r in records
        ],
    }


@router.get("/api/scan/{scan_id}")
def get_scan(scan_id: str) -> dict:
    record = DB.get_scan(scan_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Scan not found")
    return {
        "scan_id": record.id,
        "target": record.target,
        "risk_score": record.risk_score,
        "blocked": record.blocked,
        "findings_count": len(record.findings),
        "findings": record.findings,
        "created_at": _utc_iso(record.created_at),
    }


@router.get("/api/vulnerabilities")
def list_vulnerabilities(severity: str | None = Query(default=None)) -> dict:
    if severity and severity.lower() not in ALLOWED_SEVERITIES:
        raise HTTPException(status_code=400, detail="severity must be one of critical/high/medium/low")
    rows = DB.list_vulnerabilities()
    if severity:
        rows = [row for row in rows if row.severity.lower() == severity.lower()]
    return {
        "count": len(rows),
        "items": [
            {
                "id": row.id,
                "scan_id": row.scan_id,
                "title": row.title,
                "description": row.description,
                "severity": row.severity,
                "vulnerability_type": row.vulnerability_type,
                "confidence": row.confidence,
                "cvss_score": row.cvss,
                "cwe": row.cwe,
                "affected_parameter": row.parameter,
                "proof_of_concept": row.poc,
                "remediation": row.remediation,
            }
            for row in rows
        ],
    }


@router.get("/api/report/{scan_id}")
def get_report(scan_id: str) -> dict:
    record = DB.get_scan(scan_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Scan not found")
    payload = {
        "target": record.target,
        "risk_score": record.risk_score,
        "blocked": record.blocked,
        "findings": record.findings,
        "total_checks": SCANNER.checks_summary()["total_checks"],
    }
    report = REPORTER.generate_json_report(payload)
    return {
        "scan_id": scan_id,
        "formats": ["html", "pdf", "json", "csv"],
        "report": report,
    }


@router.get("/api/results")
def get_results() -> dict:
    rows = DB.list_results()
    return {
        "count": len(rows),
        "items": [
            {
                "id": row.id,
                "scan_id": row.scan_id,
                "target": row.target,
                "risk_score": row.risk_score,
                "blocked": row.blocked,
                "findings_count": row.findings_count,
                "created_at": _utc_iso(row.created_at),
            }
            for row in rows
        ],
    }
