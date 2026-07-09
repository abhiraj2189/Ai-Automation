from pydantic import BaseModel


class RendererRequest(BaseModel):

    audio: str

    subtitle: str

    videos: list[str]

    output: str = "outputs/final/final_video.mp4"


class RendererResponse(BaseModel):

    status: str

    output: str

    render_time: float