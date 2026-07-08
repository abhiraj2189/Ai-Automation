from pydantic import BaseModel


class TimelineRequest(BaseModel):
    scenes: list
    subtitles: dict
    voice: str


class TimelineResponse(BaseModel):
    timeline: list