# API Reference

## Core Endpoints

- `POST /api/scan` - Start a scan (`{"url":"https://example.com"}`)
- `GET /api/scan/{id}` - Scan details
- `GET /api/vulnerabilities` - Vulnerability list (`?severity=high`)
- `GET /api/report/{id}` - Report payload + available formats
- `GET /api/results` - Scan results list

## Compatibility Endpoints

- `GET /api/v1/health`
- `GET /api/v1/checks/summary`
- `POST /api/v1/scan`
- `POST /api/v1/scan/batch`
- `GET /api/v1/scans`

## WebSocket

- `WS /ws/alerts` - Connection + heartbeat events for real-time monitoring
