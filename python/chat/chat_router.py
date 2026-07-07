from fastapi import APIRouter
from pydantic import BaseModel

from python.chat.ollama_service import OllamaService

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)


class ChatRequest(BaseModel):
    message: str


@router.post("/")
def chat(data: ChatRequest):

    answer = OllamaService.ask(data.message)

    return {
        "success": True,
        "response": answer
    }