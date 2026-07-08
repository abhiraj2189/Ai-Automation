from pydantic import BaseModel


class AssetRequest(BaseModel):

    keyword: str

    count: int = 5


class AssetResponse(BaseModel):

    assets: list