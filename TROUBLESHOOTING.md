# Troubleshooting

## Frontend not reachable on `localhost:3000`

1. Confirm services are healthy:
   ```bash
   docker compose ps
   ```
2. Rebuild and restart:
   ```bash
   docker compose down
   docker compose up -d --build
   ```

## Backend not reachable on `localhost:8000`

Check backend health:

```bash
curl http://localhost:8000/api/health
```

## Database startup issues

```bash
docker compose logs postgres
docker compose restart postgres
```

## WebSocket disconnects

Use:

```bash
ws://localhost:8000/ws/alerts
```

The server now sends periodic heartbeat messages.
