from pydantic import BaseModel


class TimelineRequest(BaseModel):

    scenes: list

    videos: list[str]

    audio: str


class TimelineResponse(BaseModel):

    timeline: list