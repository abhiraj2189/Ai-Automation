from fastapi import APIRouter, Depends

from python.schemas.chat_schema import ChatSchema
from python.auth.auth_dependency import get_current_user
from python.ai_chat.ai_chat_service import AIChatService

router = APIRouter(
    prefix="/ai-chat",
    tags=["AI Chat"]
)


@router.post("")
def chat(
    data: ChatSchema,
    user=Depends(get_current_user)
):

    service = AIChatService()

    return service.chat(user, data)


@router.get("/history")
def history(
    user=Depends(get_current_user)
):

    service = AIChatService()

    return service.history(user)


@router.get("/conversations")
def conversations(
    user=Depends(get_current_user)
):

    service = AIChatService()

    return service.conversations(user)


@router.delete("/{conversation_id}")
def delete_conversation(
    conversation_id: str,
    user=Depends(get_current_user)
):

    service = AIChatService()

    return service.delete(
        user,
        conversation_id
    )