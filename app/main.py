from app.core.config import settings
from app.routing import (
    rest_router, 
    websocket_router
)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware



app = FastAPI(debug=True)
app.mount('/static', StaticFiles(directory='app/static'), 'static')

# if settings.all_cors_origin:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=["*"],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"]
#     )


app.include_router(rest_router)
app.include_router(websocket_router, prefix=settings.API_WEBSOCKET_STR)