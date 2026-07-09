import json
import requests

from python.config.settings import settings

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"


def generate(prompt: str, system: str = ""):

    payload = {
        "model": settings.OLLAMA_MODEL,
        "prompt": prompt,
        "system": system,
        "stream": False
    }

    print("=" * 80)
    print("MODEL :", settings.OLLAMA_MODEL)
    print("Sending request to Ollama...")

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=180
    )

    print("STATUS :", response.status_code)

    response.raise_for_status()

    data = response.json()

    print("DONE :", data.get("done"))

    text = data.get("response", "")

    print("Response Length :", len(text))

    print("=" * 80)

    return text


# ===================================================
# TEXT GENERATION
# ===================================================

def generate_text(prompt: str, system: str = ""):
    """
    Used by ResearchService and ScriptService
    """
    return generate(prompt, system)


# ===================================================
# JSON GENERATION
# ===================================================

def generate_json(prompt: str, system: str = ""):

    text = generate(prompt, system)

    print("\n================ RAW RESPONSE ================\n")
    print(text)
    print("\n==============================================\n")

    # Direct JSON
    try:
        return json.loads(text)
    except Exception:
        pass

    # JSON Object
    try:
        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1:
            return json.loads(text[start:end + 1])
    except Exception:
        pass

    # JSON Array
    try:
        start = text.find("[")
        end = text.rfind("]")

        if start != -1 and end != -1:
            return json.loads(text[start:end + 1])
    except Exception:
        pass

    raise ValueError(
        "Ollama did not return valid JSON.\n\nResponse:\n" + text
    )