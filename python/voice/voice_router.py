from fastapi import APIRouter

from python.voice.models import VoiceRequest

from python.voice.voice_service import VoiceService

router = APIRouter(

    prefix="/voice",

    tags=["Voice"]

)


@router.post("/")

def generate(data: VoiceRequest):

    service = VoiceService()

    output = "outputs/audio/output.mp3"

    audio = service.generate(

        data.text,

        output,

        data.language

    )

    return {

        "audio": audio

    }