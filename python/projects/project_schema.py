from pydantic import BaseModel


class ProjectCreate(BaseModel):
    topic: str
    research: str
    script: str
    scenes: list