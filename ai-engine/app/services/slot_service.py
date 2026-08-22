import json

from app.llm.provider import ask_llm
from app.prompts.extraction import SYSTEM_PROMPT
from app.schemas.ai_output import AIExtraction


def extract_information(message: str) -> AIExtraction:
    raw_response = ask_llm(
        prompt=message,
        system_prompt=SYSTEM_PROMPT,
    )

    data = json.loads(raw_response)

    return AIExtraction.model_validate(data)
if __name__ == "__main__":
    result = extract_information(
        "I need a deluxe room for 2 people "
        "from 2026-08-25 to 2026-08-27."
    )

    print(result.model_dump_json(indent=2))
