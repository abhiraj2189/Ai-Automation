import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    # ============================
    # AI MODEL
    # ============================

    OLLAMA_MODEL = os.getenv(
        "OLLAMA_MODEL",
        "llama3.2:3b"
    )

    # ============================
    # TELEGRAM
    # ============================

    TELEGRAM_LINK = os.getenv(
        "TELEGRAM_LINK",
        "https://t.me/your_channel"
    )

    # ============================
    # PEXELS API
    # ============================

    PEXELS_API_KEY = os.getenv(
        "PEXELS_API_KEY",
        ""
    )

    # ============================
    # OUTPUT
    # ============================

    OUTPUT_FOLDER = os.getenv(
        "OUTPUT_FOLDER",
        "outputs"
    )

    # ============================
    # VIDEO
    # ============================

    VIDEO_WIDTH = int(
        os.getenv("VIDEO_WIDTH", "1080")
    )

    VIDEO_HEIGHT = int(
        os.getenv("VIDEO_HEIGHT", "1920")
    )

    FPS = int(
        os.getenv("FPS", "30")
    )

    # ============================
    # LOGGING
    # ============================

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    # ============================
    # PIPER TTS
    # ============================

    PIPER_PATH = os.getenv(
        "PIPER_PATH",
        "tools/piper/piper.exe"
    )

    ENGLISH_MODEL = os.getenv(
        "ENGLISH_MODEL",
        "voices/english/en_US-medium.onnx"
    )

    HINDI_MODEL = os.getenv(
        "HINDI_MODEL",
        "voices/hindi/hi_IN-medium.onnx"
    )

    HINGLISH_MODEL = os.getenv(
        "HINGLISH_MODEL",
        "voices/hinglish/hinglish.onnx"
    )


settings = Settings()