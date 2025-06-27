from pydantic import BaseModel


class SignalingDataDTO(BaseModel):
    sdp: str
    type: str
    video_transform: str

    