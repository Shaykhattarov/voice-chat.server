from fastapi import APIRouter
from starlette.responses import PlainTextResponse


router = APIRouter(prefix='/hello', tags=['Hello'])


@router.get('/')
async def hello_message():
    return PlainTextResponse(content="Hello world!", status_code=200)