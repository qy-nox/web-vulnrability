from fastapi.testclient import TestClient

from src.api.app import app
from src.api import routes


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_checks_summary_endpoint() -> None:
    response = client.get("/api/v1/checks/summary")
    assert response.status_code == 200
    data = response.json()
    assert data["total_checks"] >= 2500
    assert data["tier_count"] >= 20


def test_scan_and_results_endpoints() -> None:
    response = client.post("/api/scan", json={"url": "https://example.com"})
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "completed"
    assert payload["scan_id"].startswith("scan-")

    scan_id = payload["scan_id"]

    detail = client.get(f"/api/scan/{scan_id}")
    assert detail.status_code == 200
    assert detail.json()["scan_id"] == scan_id

    vulnerabilities = client.get("/api/vulnerabilities")
    assert vulnerabilities.status_code == 200
    assert vulnerabilities.json()["count"] >= 1
    first = vulnerabilities.json()["items"][0]
    assert "vulnerability_type" in first
    assert "confidence" in first
    invalid_filter = client.get("/api/vulnerabilities?severity=invalid")
    assert invalid_filter.status_code == 400

    report = client.get(f"/api/report/{scan_id}")
    assert report.status_code == 200
    assert "json" in report.json()["formats"]

    results = client.get("/api/results")
    assert results.status_code == 200
    assert results.json()["count"] >= 1


def test_scan_handles_internal_errors(monkeypatch) -> None:
    def _raise(_target: str):
        raise RuntimeError("scanner failure")

    monkeypatch.setattr(routes.SCANNER, "scan_target", _raise)
    response = client.post("/api/scan", json={"url": "https://example.com"})
    assert response.status_code == 500
    assert "Scan execution failed" in response.json()["detail"]


def test_batch_scan_continues_when_a_target_fails(monkeypatch) -> None:
    original = routes.SCANNER.scan_target

    def _scan_target(target: str):
        if "bad.example" in target:
            raise RuntimeError("forced failure")
        return original(target)

    monkeypatch.setattr(routes.SCANNER, "scan_target", _scan_target)
    response = client.post(
        "/api/v1/scan/batch",
        json={"urls": ["https://example.com", "https://bad.example.com"]},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["count"] == 2
    assert payload["results"][0]["status"] == "completed"
    assert payload["results"][1]["status"] == "failed"
