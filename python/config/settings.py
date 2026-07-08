import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    # ============================
    # AI MODEL
    # ============================

    OLLAMA_MODEL = os.getenv(
        "OLLAMA_MODEL",
        "qwen2.5:7b-instruct"
    )

    # ============================
    # TELEGRAM
    # ============================

    TELEGRAM_LINK = os.getenv(
        "TELEGRAM_LINK",
        "https://t.me/your_channel"
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


settings = Settings()