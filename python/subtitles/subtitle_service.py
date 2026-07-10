from python.subtitles.whisper_service import WhisperService


class SubtitleService:

    def generate(self, audio):

        whisper = WhisperService()

        result = whisper.transcribe(audio)

        return {
            "subtitle": result,
            "segments": result["segments"],
            "text": result["text"]
        }