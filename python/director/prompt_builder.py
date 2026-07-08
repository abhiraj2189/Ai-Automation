class PromptBuilder:

    @staticmethod
    def build(script: str):

        return f"""
You are a Professional Short Video Director.

Analyze this script.

Return ONLY JSON.

{{
    "hook_style":"",
    "bgm":"",
    "caption_style":"",
    "transitions":[],
    "effects":[],
    "camera":[]
}}

Script:

{script}
"""