#!/bin/bash

# Color Definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to display progress
progress() {
  echo -n -e "${YELLOW}[$(date +'%H:%M:%S')] $1...${NC}\n"
}

# Check Docker and Docker Compose are installed
if ! command -v docker &> /dev/null || ! command -v docker-compose &> /dev/null; then
  echo -e "${RED}Docker and Docker Compose must be installed!${NC}"
  exit 1
fi

echo -e "${GREEN}Docker and Docker Compose are installed.${NC}"

# Setup .env file
echo -e "${BLUE}Setting up .env file...${NC}"
cat <<EOT > .env
# Environment Variables
DB_NAME=web_vuln_db
DB_USER=user
DB_PASSWORD=password
REDIS_URL=redis://redis:6379
RABBITMQ_URL=amqp://guest:guest@rabbitmq:5672/
ELASTICSEARCH_URL=http://elasticsearch:9200
EOT

echo -e "${GREEN}.env file created.${NC}"

# Build Docker images
progress "Building Docker images"
docker-compose build

# Start all services
progress "Starting all services"
docker-compose up -d

# Wait for services to be ready
progress "Waiting for services to be ready"
sleep 30 # Adjust as necessary for your services' startup time

# Initialize database
progress "Initializing database"
docker-compose exec backend python manage.py migrate

# Display access information and credentials
echo -e "${GREEN}Services are up and running!${NC}"
echo -e "${BLUE}Access Information:${NC}"
echo -e "${BLUE}Frontend: http://localhost:3000${NC}"
echo -e "${BLUE}Backend: http://localhost:8000${NC}"
echo -e "${BLUE}Database: ${DB_USER}/${DB_PASSWORD}@localhost:5432/${DB_NAME}${NC}"

# Auto-open browser
open http://localhost:3000 # Use 'xdg-open' for Linux

# Show helpful commands and troubleshooting tips
echo -e "${YELLOW}Helpful Commands:${NC}"
echo -e "${YELLOW}docker-compose up -d  : Start services${NC}"
echo -e "${YELLOW}docker-compose down     : Stop services${NC}"
echo -e "${YELLOW}docker-compose logs     : View logs${NC}"
