#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="${ROOT_DIR}/backend"

if [[ "${1:-}" == "--help" ]]; then
  echo "Usage: ./run.sh [--docker]"
  echo "  (default)  Install backend deps (if needed) and run FastAPI locally on :8000"
  echo "  --docker   Run backend via docker compose on :8000"
  exit 0
fi

if [[ "${1:-}" == "--docker" ]]; then
  docker compose -f "${ROOT_DIR}/docker-compose.yml" up --build
  exit 0
fi

cd "${BACKEND_DIR}"
python -m pip install -r requirements.txt
PYTHONPATH=. uvicorn src.api.app:app --host 0.0.0.0 --port 8000 --reload
