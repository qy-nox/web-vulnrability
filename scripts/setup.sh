#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BACKEND_REQS="${ROOT_DIR}/backend/requirements.txt"

echo "[1/2] Installing backend dependencies"
if [[ ! -f "${BACKEND_REQS}" ]]; then
  echo "Missing requirements file: ${BACKEND_REQS}" >&2
  exit 1
fi
python3 -m pip install -r "${BACKEND_REQS}"

if [[ -f "${ROOT_DIR}/frontend/package.json" ]]; then
  echo "[2/2] Installing frontend dependencies"
  (cd "${ROOT_DIR}/frontend" && npm install)
fi

echo "Setup complete."
echo "Run backend locally: ./run.sh"
echo "Run backend with Docker: ./run.sh --docker"
