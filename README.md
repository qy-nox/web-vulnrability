# Advanced Enterprise Web Vulnerability Detection & Blocking System

This repository now includes an enterprise-grade scaffold for a web vulnerability platform with:

- **1020 checks** across **10 tiers** (zero-day, API, cloud, ML, network, client-side, auth/session, business logic, SSL/TLS, compliance)
- **FastAPI backend** with single and batch scan endpoints
- **Real-time monitoring stub** using WebSocket alerts
- **Risk scoring + CVSS base score + exploit chain suggestion**
- **Compliance mapping** for HIPAA/GDPR/PCI-DSS/ISO 27001
- **Professional dashboard scaffold** (React TypeScript components + mock enterprise UI page)

## Project Structure

```text
web-vulnrability/
├── backend/
│   ├── src/
│   │   ├── core/
│   │   ├── scanners/
│   │   ├── firewall/
│   │   ├── api/
│   │   ├── reporting/
│   │   ├── database/
│   │   └── utils/
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── docker-compose.yml
├── frontend/
│   ├── src/components/
│   ├── package.json
│   ├── tsconfig.json
│   ├── Dockerfile
│   └── mock_dashboard.html
├── ml_models/
├── kubernetes/
├── docs/
└── docker-compose.yml
```

## Quick Start (Backend)

```bash
cd backend
python -m pip install -r requirements.txt
PYTHONPATH=. uvicorn src.api.app:app --reload
```

## Key API Endpoints

- `GET /api/v1/health`
- `GET /api/v1/checks/summary`
- `POST /api/v1/scan`
- `POST /api/v1/scan/batch`
- `GET /api/v1/scans`
- `WS /ws/alerts`

## Testing

```bash
cd backend
PYTHONPATH=. pytest -q
```
