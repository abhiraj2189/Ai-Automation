from pydantic import BaseModel


class ChatSchema(BaseModel):
    message: str
    conversation_id: str