# Setup Script for web-vulnrability

## setup.sh (Linux/Mac)

```bash
#!/bin/bash

# Update package lists and install Docker
if ! command -v docker &> /dev/null
then
    echo "Docker not found. Installing Docker..."
    sudo apt-get update
    sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install -y docker-ce
fi

# Clone the repository
git clone https://github.com/your_username/web-vulnrability.git
cd web-vulnrability

# Copy .env.example to .env
cp .env.example .env

# Initialize Database
docker-compose up -d db
# You might need to wait until the database is ready
sleep 10 

# Run database migrations
docker-compose exec app php artisan migrate

# Start all services
docker-compose up -d
```

## setup.bat (Windows)

```bat
@echo off

REM Check if Docker is installed
where docker >nul 2>&1
if %errorlevel% neq 0 (
    echo Docker not found. Please install Docker Desktop for Windows.
    exit /b
)

REM Clone the repository
git clone https://github.com/your_username/web-vulnrability.git
cd web-vulnrability

REM Copy .env.example to .env
copy .env.example .env

REM Initialize Database
docker-compose up -d db
REM Delay to ensure database is ready
timeout /t 10

REM Run database migrations
docker-compose exec app php artisan migrate

REM Start all services
docker-compose up -d
```
