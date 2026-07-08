from pydantic import BaseModel


class DirectorRequest(BaseModel):
    topic: str
    script: str


class DirectorResponse(BaseModel):
    hook_style: str
    bgm: str
    caption_style: str
    transitions: list
    effects: list
    camera: list