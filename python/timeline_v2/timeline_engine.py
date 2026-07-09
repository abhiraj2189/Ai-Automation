import os

from moviepy import AudioFileClip


class TimelineEngine:

    def generate(

        self,

        scenes,

        videos,

        audio

    ):

        audio_clip = AudioFileClip(audio)

        duration = audio_clip.duration

        per_scene = duration / len(scenes)

        timeline = []

        index = 0

        for scene in scenes:

            video = videos[index % len(videos)]

            timeline.append({

                "scene": scene,

                "video": video,

                "start": round(index * per_scene, 2),

                "end": round((index + 1) * per_scene, 2)

            })

            index += 1

        return {

            "timeline": timeline,

            "duration": duration

        }