# Advanced Enterprise Web Vulnerability Detection & Blocking System

This repository now includes an enterprise-grade scaffold for a web vulnerability platform with:

- **2000+ checks** across foundational + advanced scanner modules (zero-day, API, cloud, ML, network, client-side, auth/session, business logic, SSL/TLS, compliance, CloudFlare/WAF bypass, XXE/deserialization, SSRF, dependencies, WebSocket, JavaScript/DOM and more)
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

## Setup

### Linux/macOS

```bash
chmod +x scripts/setup.sh run.sh
./scripts/setup.sh
```

### Windows (PowerShell/CMD)

```bat
python -m pip install -r backend\requirements.txt
cd frontend && npm install && cd ..
```

## Run

### Local backend (recommended)

```bash
./run.sh
```

Windows:

```bat
run.bat
```

### Docker backend

```bash
./run.sh --docker
```

The backend is available at `http://localhost:8000`.

### Frontend scaffold

The frontend is currently a scaffold. The configured scripts are placeholders:

```bash
cd frontend
npm run test
npm run build
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
