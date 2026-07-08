from pydantic import BaseModel


class VoiceRequest(BaseModel):
    text: str
    voice: str = "default"