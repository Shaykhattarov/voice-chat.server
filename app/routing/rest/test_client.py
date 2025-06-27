from fastapi import APIRouter
from starlette.responses import PlainTextResponse

from app.dto.sdp import SignalingDataDTO



router = APIRouter(prefix='/offer', tags=['Offer'])


@router.post('/')
async def offer(signaling_data: SignalingDataDTO):
    
    params = await signaling_data
