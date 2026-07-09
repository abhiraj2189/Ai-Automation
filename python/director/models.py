from pydantic import BaseModel


class DirectorRequest(BaseModel):

    script: str


class DirectorResponse(BaseModel):

    scenes: list