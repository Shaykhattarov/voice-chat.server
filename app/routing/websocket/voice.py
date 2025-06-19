from fastapi import APIRouter, WebSocket



router = APIRouter(prefix="/voice", tags=["Voice"])


@router.websocket("/recieve")
async def receive_client_voice(websocket: WebSocket):
    await websocket.accept()
    while True:
        voice = await websocket.receive_bytes()
        print(voice)
        await websocket.send_text("Данные получены!")
