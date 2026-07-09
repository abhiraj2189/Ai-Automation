class Planner:

    def build(

        self,

        scenes

    ):

        plan = []

        for i, scene in enumerate(scenes):

            plan.append({

                "scene": i + 1,

                "text": scene,

                "camera": "zoom_in",

                "transition": "fade",

                "effect": "cinematic",

                "caption": "word_by_word",

                "music": "soft",

                "duration": 4

            })

        return plan