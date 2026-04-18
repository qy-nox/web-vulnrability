#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="${ROOT_DIR}/backend"
COMPOSE_FILE="${ROOT_DIR}/docker-compose.yml"
HEALTH_CHECK_MAX_ATTEMPTS="${HEALTH_CHECK_MAX_ATTEMPTS:-40}"

if [[ "${1:-}" == "--help" ]]; then
  echo "Usage: ./run.sh [--docker]"
  echo "  (default)  Install backend deps (if needed) and run FastAPI locally on :8000"
  echo "  --docker   Run dockerized stack (postgres -> backend -> frontend)"
  exit 0
fi

if [[ "${1:-}" == "--docker" ]]; then
  if ! command -v docker >/dev/null 2>&1; then
    echo "Docker is required but not installed." >&2
    exit 1
  fi

  if ! docker info >/dev/null 2>&1; then
    echo "Docker daemon is not running. Start Docker and retry." >&2
    exit 1
  fi

  if [[ ! -f "${ROOT_DIR}/.env" ]]; then
    cp "${ROOT_DIR}/.env.example" "${ROOT_DIR}/.env"
  fi

  echo "[1/7] Building backend and frontend images"
  docker compose -f "${COMPOSE_FILE}" build backend frontend

  echo "[2/7] Starting database"
  docker compose -f "${COMPOSE_FILE}" up -d postgres

  echo "[3/7] Starting backend API"
  docker compose -f "${COMPOSE_FILE}" up -d backend

  echo "[4/7] Starting frontend"
  docker compose -f "${COMPOSE_FILE}" up -d frontend

  echo "[5/7] Waiting for health checks"
  for service in postgres backend frontend; do
    cid="$(docker compose -f "${COMPOSE_FILE}" ps -q "${service}")"
    for ((i=0; i<HEALTH_CHECK_MAX_ATTEMPTS; i++)); do
      state="$(docker inspect -f '{{if .State.Health}}{{.State.Health.Status}}{{else}}{{.State.Status}}{{end}}' "${cid}")"
      if [[ "${state}" == "healthy" || "${state}" == "running" ]]; then
        break
      fi
      sleep 2
    done
    if [[ "${state}" != "healthy" && "${state}" != "running" ]]; then
      echo "Service '${service}' did not become healthy in time." >&2
      exit 1
    fi
  done

  echo "[6/7] Initializing database schema"
  docker compose -f "${COMPOSE_FILE}" exec -T backend python - <<'PY'
from src.database.db_manager import InMemoryDBManager
print(InMemoryDBManager().initialize_schema())
PY

  echo "[7/7] Verifying service connectivity"
  python3 - <<'PY'
import urllib.request
import urllib.error
checks = {
    "frontend": "http://localhost:3000",
    "backend": "http://localhost:8000/api/health",
}
for name, url in checks.items():
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            print(f"{name}: {response.status}")
    except urllib.error.URLError as exc:
        raise SystemExit(f"{name} connectivity check failed for {url}: {exc}")
PY

  echo
  echo "Frontend: http://localhost:3000"
  echo "Backend:  http://localhost:8000"
  echo "Docs:     http://localhost:8000/docs"
  exit 0
fi

cd "${BACKEND_DIR}"
python3 -m pip install -r requirements.txt
PYTHONPATH=. uvicorn src.api.app:app --host 127.0.0.1 --port 8000 --reload
