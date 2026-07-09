from pydantic import BaseModel


class RenderRequest(BaseModel):

    video_paths: list[str]

    audio_path: str

    subtitle_path: str

    output: str = "outputs/final/final_video.mp4"