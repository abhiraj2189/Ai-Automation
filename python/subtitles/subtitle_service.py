from python.subtitles.whisper_service import WhisperService


class SubtitleService:

    def generate(self, audio):

        whisper = WhisperService()

        return whisper.transcribe(audio)