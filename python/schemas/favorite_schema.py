from pydantic import BaseModel


class FavoriteSchema(BaseModel):
    tool_name: str
    website: str