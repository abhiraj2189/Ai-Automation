import os

from moviepy import AudioFileClip


class AudioMixer:

    def load(
        self,
        audio_path: str
    ):

        if not os.path.exists(audio_path):
            raise FileNotFoundError(
                f"Audio not found : {audio_path}"
            )

        return AudioFileClip(audio_path)

    def attach(
        self,
        video,
        audio_path: str
    ):

        audio = self.load(audio_path)

        # Trim audio if longer than video
        if audio.duration > video.duration:
            audio = audio.subclipped(
                0,
                video.duration
            )

        # Trim video if longer than audio
        elif video.duration > audio.duration:
            video = video.subclipped(
                0,
                audio.duration
            )

        video = video.with_audio(audio)

        return video

    def duration(
        self,
        audio_path: str
    ):

        audio = self.load(audio_path)

        d = audio.duration

        audio.close()

        return d