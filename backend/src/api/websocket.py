import asyncio

from fastapi import APIRouter, WebSocket
from starlette.websockets import WebSocketDisconnect

router = APIRouter()


@router.websocket("/ws/alerts")
async def alerts_socket(websocket: WebSocket) -> None:
    await websocket.accept()
    await websocket.send_json({"event": "connected", "message": "Real-time monitoring active"})
    try:
        while True:
            await websocket.send_json({"event": "heartbeat", "message": "scanner-ready"})
            await asyncio.sleep(5)
    except WebSocketDisconnect:
        return
