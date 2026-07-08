from fastapi import APIRouter

from python.voice.voice_schema import VoiceRequest
from python.voice.voice_service import VoiceService

router = APIRouter(
    prefix="/voice",
    tags=["Voice"]
)


@router.post("/")
def generate_voice(data: VoiceRequest):

    service = VoiceService()

    return service.generate(data.text)