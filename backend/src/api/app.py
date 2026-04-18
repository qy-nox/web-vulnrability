from fastapi import FastAPI

from src.api.routes import router as api_router
from src.api.websocket import router as ws_router
from src.core.advanced_scanner import SCANNER

app = FastAPI(title="Enterprise Web Vulnerability Detection & Blocking System")
app.include_router(api_router)
app.include_router(ws_router)


@app.get("/")
def root() -> dict:
    summary = SCANNER.checks_summary()
    return {
        "name": "Advanced Enterprise Vulnerability Detection",
        "version": "1.0.0",
        "checks": summary["total_checks"],
        "tiers": summary["tier_count"],
    }
