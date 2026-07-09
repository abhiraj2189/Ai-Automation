import os
from moviepy import AudioFileClip


class TimelineEngine:

    def generate(

        self,

        scenes,

        videos,

        audio

    ):

        if not scenes:
            raise Exception("No scenes found.")

        if not videos:
            raise Exception("No videos found.")

        if not os.path.exists(audio):
            raise Exception("Audio file not found.")

        audio_clip = AudioFileClip(audio)

        total_duration = audio_clip.duration

        timeline = []

        current = 0

        per_scene = total_duration / len(scenes)

        for index, scene in enumerate(scenes):

            video = videos[index % len(videos)]

            start = round(current, 2)

            end = round(current + per_scene, 2)

            timeline.append({

                "scene": index + 1,

                "video": video,

                "start": start,

                "end": end,

                "duration": round(per_scene, 2),

                "voice": scene.get("voice", ""),

                "caption": scene.get("caption", ""),

                "visual": scene.get("visual", ""),

                "animation": scene.get(

                    "animation",

                    "zoom"

                ),

                "transition": scene.get(

                    "transition",

                    "fade"

                )

            })

            current += per_scene

        return {

            "duration": round(total_duration, 2),

            "total_scenes": len(timeline),

            "timeline": timeline

        }