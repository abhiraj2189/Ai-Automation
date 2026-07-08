from pydantic import BaseModel


class VideoRequest(BaseModel):

    timeline: dict

    voice: str


class VideoResponse(BaseModel):

    output: str