class PromptBuilder:

    @staticmethod
    def build(research: str):

        return f"""
You are an expert Tech YouTube Script Writer.

Using the research below, create a professional YouTube Shorts / Instagram Reel script.

Research:

{research}

Requirements:

- Language: Hinglish
- Duration: 45-60 seconds
- Start with a powerful hook
- Explain simply
- Use storytelling
- Include one real-life example
- End with a strong CTA

Return only the script.
"""