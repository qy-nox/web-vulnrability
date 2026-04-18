@echo off
setlocal

if "%1"=="--docker" (
  docker compose -f docker-compose.yml up --build
  exit /b %errorlevel%
)

cd /d backend
python -m pip install -r requirements.txt
if errorlevel 1 exit /b %errorlevel%

set PYTHONPATH=.
python -m uvicorn src.api.app:app --host 0.0.0.0 --port 8000 --reload
