from fastapi import APIRouter
from pydantic import BaseModel

from python.scene.scene_service import SceneService

router = APIRouter(
    prefix="/scene",
    tags=["Scene Generator"]
)


class SceneRequest(BaseModel):
    script: str


@router.post("/")
def generate_scene(data: SceneRequest):

    service = SceneService()

    scenes = service.generate_scene(data.script)

    return {
        "success": True,
        "scenes": scenes
    }