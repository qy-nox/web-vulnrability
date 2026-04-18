from fastapi import APIRouter, WebSocket

router = APIRouter()


@router.websocket("/ws/alerts")
async def alerts_socket(websocket: WebSocket) -> None:
    await websocket.accept()
    await websocket.send_json({"event": "connected", "message": "Real-time monitoring active"})
    await websocket.close()
