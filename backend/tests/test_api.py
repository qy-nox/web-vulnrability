from fastapi.testclient import TestClient

from src.api.app import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_checks_summary_endpoint() -> None:
    response = client.get("/api/v1/checks/summary")
    assert response.status_code == 200
    data = response.json()
    assert data["total_checks"] >= 1000
    assert data["tier_count"] == 10
