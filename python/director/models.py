from pydantic import BaseModel


class DirectorRequest(BaseModel):

    topic: str

    script: str

    scenes: list


class DirectorResponse(BaseModel):

    storyboard: list