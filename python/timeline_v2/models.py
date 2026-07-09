from pydantic import BaseModel


class TimelineRequest(BaseModel):

    scenes: list

    videos: list[str]

    audio: str


class TimelineResponse(BaseModel):

    duration: float

    total_scenes: int

    timeline: list