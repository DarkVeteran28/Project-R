import httpx


OLLAMA_URL = "http://localhost:11434/api/chat"

MODEL_NAME = "qwen3:8b"


def ask_llm(prompt: str, system_prompt: str | None = None) -> str:
    messages = []

    if system_prompt:
        messages.append(
            {
                "role": "system",
                "content": system_prompt,
            }
        )

    messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0,
        },
    }

    response = httpx.post(
        OLLAMA_URL,
        json=payload,
        timeout=120.0,
    )

    response.raise_for_status()

    data = response.json()

    return data["message"]["content"]
if __name__ == "__main__":
    result = ask_llm(
        "Return exactly this JSON: {\"status\": \"ok\"}"
    )

    print(result)