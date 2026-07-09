from pydantic import BaseModel


class PlannerRequest(BaseModel):

    scenes: list


class PlannerResponse(BaseModel):

    assets: list