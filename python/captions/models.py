from pydantic import BaseModel


class CaptionRequest(BaseModel):

    subtitle_file: str

    style: str = "word_by_word"


class CaptionResponse(BaseModel):

    output: str