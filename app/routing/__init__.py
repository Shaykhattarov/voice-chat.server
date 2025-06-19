from fastapi import APIRouter

from app.routing.rest import hello
from app.routing.websocket import voice

rest_router = APIRouter()
websocket_router = APIRouter()

rest_router.include_router(hello.router)

websocket_router.include_router(voice.router)