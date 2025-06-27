from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates




router = APIRouter(tags=['Index'])
templates = Jinja2Templates(directory="app/static/templates")


@router.get('/')
async def index(request: Request):
    return templates.TemplateResponse(name="index.html", media_type="text/html", context={'request': request})