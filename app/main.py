from app.core.config import settings
from app.routing import (
    rest_router, 
    websocket_router
)

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware



app = FastAPI(debug=True)


if settings.all_cors_origin:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origin,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )


app.include_router(rest_router, prefix=settings.API_REST_STR)
app.include_router(websocket_router, prefix=settings.API_WEBSOCKET_STR)