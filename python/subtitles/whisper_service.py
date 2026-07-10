import whisper


class WhisperService:

    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe(self, audio):

        result = self.model.transcribe(
            audio,
            word_timestamps=True
        )

        return {
            "subtitle": result,
            "segments": result.get("segments", []),
            "text": result.get("text", "")
        }