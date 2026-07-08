class SceneTimeline:

    def build(self, scenes):

        timeline = []

        start = 0

        for scene in scenes:

            duration = scene.get("duration", 3)

            timeline.append({

                "start": start,

                "end": start + duration,

                "scene": scene

            })

            start += duration

        return timeline