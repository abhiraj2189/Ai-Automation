from pydantic import BaseModel


class ComposerRequest(BaseModel):

    audio: str

    subtitle: str

    videos: list[str]

    output: str = "outputs/final/final_video.mp4"