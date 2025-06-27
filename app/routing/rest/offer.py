import uuid
import logging

from app.dto.sdp import SignalingDataDTO

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from aiortc import (
    RTCSessionDescription,
    RTCPeerConnection
)
from aiortc.contrib.media import (
    MediaPlayer,
    MediaRecorder,
    MediaRelay,
    MediaBlackhole,
)



router = APIRouter(prefix='/offer', tags=['Offer'])


@router.post('/')
async def offer_endpoint(request: Request):
    relay = MediaRelay()
    logging.basicConfig(level=logging.DEBUG)

    params = await request.json()
    offer = RTCSessionDescription(
        sdp=params['sdp'],
        type=params['type']
    )

    pc = RTCPeerConnection()
    pc_id = f"Peer Connection({uuid.uuid4()})"

    print(f"[INFO] Created for ({request.client.host}:{request.client.port})")

    # prepare local media
    player = MediaPlayer(file="app/static/media/output2.mp4")
    recorder = MediaRecorder(file="app/static/media/saved.mp4")
    
    @pc.on('datachannel')
    async def on_datachannel(channel):
        @channel.on("message")
        async def on_message(message):
            if isinstance(message, str) and message.startswith("ping"):
                channel.send("pong" + message[4:])

    @pc.on("connectionstatechange")
    async def on_connectionstatechange():
        print(f"Connection state is {pc.connectionState}")
        if pc.connectionState == "failed":
            await pc.close()
            # pcs.discard(pc)

    @pc.on("track")
    async def on_track(track):
        print(f"Track {track.kind} received")

        if track.kind == "audio":
            pc.addTrack(player.audio)
            recorder.addTrack(track)
        elif track.kind == "video":
            pc.addTrack(
                track
            )
            recorder.addTrack(relay.subscribe(track))

        @track.on("ended")
        async def on_ended():
            print(f"Track {track.kind} ended")
            await recorder.stop()

    # handle offer
    await pc.setRemoteDescription(offer)
    await recorder.start()

    # send answer
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return JSONResponse(
        content={
            'sdp': pc.localDescription.sdp,
            'type': pc.localDescription.type
        }
    )