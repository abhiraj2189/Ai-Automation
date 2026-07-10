import json
import requests

from python.config.settings import settings

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"


def generate(prompt: str, system: str = ""):

    payload = {
        "model": settings.OLLAMA_MODEL,
        "prompt": prompt,
        "system": system,
        "stream": False,
        "options": {
            "temperature": 0.4,
            "num_predict": 2048,
        },
    }

    print("=" * 80)
    print("MODEL :", settings.OLLAMA_MODEL)
    print("Prompt Length :", len(prompt))
    print("Sending request to Ollama...")
    print(payload)

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=600
    )

    print("STATUS :", response.status_code)

    response.raise_for_status()

    data = response.json()

    print("DONE :", data.get("done"))
    print("TOTAL DURATION :", data.get("total_duration"))

    text = data.get("response", "")

    print("Response Length :", len(text))
    print("=" * 80)

    return text


def generate_text(prompt: str, system: str = ""):
    return generate(prompt, system)


def generate_json(prompt: str, system: str = ""):

    text = generate(prompt, system)

    try:
        return json.loads(text)
    except:
        pass

    try:
        start = text.index("{")
        end = text.rindex("}") + 1
        return json.loads(text[start:end])
    except:
        pass

    try:
        start = text.index("[")
        end = text.rindex("]") + 1
        return json.loads(text[start:end])
    except:
        pass

    raise Exception(text)