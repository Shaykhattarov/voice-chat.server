from fastapi import APIRouter

from app.routing.rest import (
    index,
    offer
)

# from app.routing.websocket import voice

rest_router = APIRouter()
websocket_router = APIRouter()

rest_router.include_router(offer.router)
rest_router.include_router(index.router)

# websocket_router.include_router(voice.router)