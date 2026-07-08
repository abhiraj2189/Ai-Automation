import re


class LanguageDetector:

    @staticmethod
    def detect(text: str) -> str:

        # Hindi Unicode
        if re.search(r'[\u0900-\u097F]', text):
            return "hindi"

        # Hinglish keywords
        hinglish_words = [
            "bhai",
            "kaise",
            "kya",
            "hai",
            "kar",
            "kr",
            "aur",
            "nahi",
            "video",
            "python",
            "chatgpt"
        ]

        lower = text.lower()

        for word in hinglish_words:
            if word in lower:
                return "hinglish"

        return "english"