from pydantic import BaseModel


class SelectorRequest(BaseModel):

    keyword: str

    videos: list


class SelectorResponse(BaseModel):

    best_video: dict