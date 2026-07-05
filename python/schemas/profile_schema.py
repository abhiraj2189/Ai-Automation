from pydantic import BaseModel

class ProfileSchema(BaseModel):
    username: str
    email: str