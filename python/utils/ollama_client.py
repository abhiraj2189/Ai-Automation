import json
import re
import ollama

from python.config.settings import settings

DEFAULT_MODEL = settings.OLLAMA_MODEL


def _clean_json(text: str) -> str:
    """
    Remove markdown code fences and extract JSON.
    """

    text = text.strip()

    # Remove markdown fences
    text = re.sub(r"^```json", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^```", "", text)
    text = re.sub(r"```$", "", text)

    text = text.strip()

    # JSON Array
    start_array = text.find("[")
    end_array = text.rfind("]")

    if start_array != -1 and end_array != -1:
        return text[start_array:end_array + 1]

    # JSON Object
    start_obj = text.find("{")
    end_obj = text.rfind("}")

    if start_obj != -1 and end_obj != -1:
        return text[start_obj:end_obj + 1]

    return text


def generate_text(
    prompt: str,
    system: str = "",
    model: str = DEFAULT_MODEL
):

    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def generate_json(
    prompt: str,
    system: str = "",
    model: str = DEFAULT_MODEL,
    retries: int = 2
):

    system_prompt = f"""
{system}

Return ONLY VALID JSON.

No markdown.

No explanation.

No comments.
"""

    current_prompt = prompt

    for _ in range(retries + 1):

        response = generate_text(
            prompt=current_prompt,
            system=system_prompt,
            model=model
        )

        cleaned = _clean_json(response)

        try:

            return json.loads(cleaned)

        except Exception as e:

            current_prompt = f"""
Your previous response was INVALID JSON.

JSON Error:

{e}

Previous Output:

{response}

Return ONLY corrected VALID JSON.
"""

    raise ValueError("Unable to generate valid JSON.")