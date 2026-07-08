from pydantic import BaseModel


class SubtitleRequest(BaseModel):
    audio: str


class SubtitleResponse(BaseModel):
    subtitles: list