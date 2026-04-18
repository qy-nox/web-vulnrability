from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import router as api_router
from src.api.websocket import router as ws_router
from src.core.advanced_scanner import SCANNER

app = FastAPI(title="Enterprise Web Vulnerability Detection & Blocking System")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
