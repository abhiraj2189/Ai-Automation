class PromptBuilder:

    @staticmethod
    def build(research: str) -> str:

        return f"""
Research:
{research}

Task:
Write a YouTube Shorts script based on the research above.

STRICT LANGUAGE RULES:
- Write in Hinglish (Hindi + English mix)
- Exactly like Indian YouTubers speak
- Hindi sentence structure, English technical words
- Example style: "Aaj hum baat karenge Python ke baare mein, jo ek bahut powerful programming language hai"
- NEVER write in pure Hindi or pure English
- Roman script only (no Devanagari)

STRICT FORMAT RULES:
- Start with a shocking fact or curiosity hook
- No greetings (no Hi, Hello, Welcome)
- Short punchy sentences
- Maximum 60 seconds when spoken
- Return only the script, nothing else
"""