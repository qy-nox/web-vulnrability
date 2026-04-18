# Setup Instructions

## Prerequisites

- Python 3.11+
- Node.js 18+
- (Optional) Docker

## Quick setup (Linux/macOS)

```bash
chmod +x scripts/setup.sh run.sh
./scripts/setup.sh
```

## Run backend

```bash
./run.sh
```

## Run backend with Docker

```bash
./run.sh --docker
```

## Validate installation

```bash
curl http://localhost:8000/api/v1/health
```
