from pydantic import BaseModel


class VoiceRequest(BaseModel):

    text: str

    language: str = "hindi_male"


class VoiceResponse(BaseModel):

    audio: str