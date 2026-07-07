from fastapi import APIRouter
from pydantic import BaseModel

from python.script.script_service import ScriptService

router = APIRouter(
    prefix="/script",
    tags=["AI Script"]
)


class ScriptRequest(BaseModel):
    topic: str


@router.post("/")
def generate_script(data: ScriptRequest):

    service = ScriptService()

    script = service.generate_script(data.topic)

    return {
        "success": True,
        "topic": data.topic,
        "script": script
    }