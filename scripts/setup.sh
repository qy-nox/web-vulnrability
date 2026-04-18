#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "[1/2] Installing backend dependencies"
python -m pip install -r "${ROOT_DIR}/backend/requirements.txt"

if [[ -f "${ROOT_DIR}/frontend/package.json" ]]; then
  echo "[2/2] Installing frontend dependencies"
  (cd "${ROOT_DIR}/frontend" && npm install)
fi

echo "Setup complete."
echo "Run backend locally: ${ROOT_DIR}/run.sh"
echo "Run backend with Docker: ${ROOT_DIR}/run.sh --docker"
