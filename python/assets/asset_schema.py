from pydantic import BaseModel


class AssetRequest(BaseModel):
    scenes: list