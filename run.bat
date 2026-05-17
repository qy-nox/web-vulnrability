@echo off
setlocal
set ROOT_DIR=%~dp0
if "%ROOT_DIR:~-1%"=="\" set ROOT_DIR=%ROOT_DIR:~0,-1%

if "%1"=="--help" (
  echo Usage: run.bat [--docker]
  echo   default  Install backend deps and run FastAPI locally on :8000
  echo   --docker Run dockerized stack
  exit /b 0
)

if "%1"=="--docker" (
  docker info >nul 2>&1
  if errorlevel 1 (
    echo Docker is required and the daemon must be running.
    exit /b 1
  )
  docker compose -f "%ROOT_DIR%\docker-compose.yml" up --build
  exit /b %errorlevel%
)

cd /d "%ROOT_DIR%\backend"
if errorlevel 1 exit /b %errorlevel%

python -m pip install -r requirements.txt
if errorlevel 1 exit /b %errorlevel%

set PYTHONPATH=.
python -m uvicorn src.api.app:app --host 127.0.0.1 --port 8000 --reload
