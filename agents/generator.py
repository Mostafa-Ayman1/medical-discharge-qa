from services.openai_client import client
from utils.helpers import load_prompt
from utils.logger import log
from config import OPENAI_MODEL


SYSTEM_PROMPT = load_prompt("generator.txt")


def run(operation: str) -> str:
    """
    Generate post-operative discharge instructions.
    """

    print("=" * 60)
    print("🏥 Generator Started")
    print(f"Operation: {operation}")

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": operation,
            },
        ],
    )

    instructions = response.output_text.strip()

    log(
        f"""
            GENERATOR

            Operation:
            {operation}

            Generated Instructions:

            {instructions}
            """
    )

    print("✅ Generator Finished")

    return instructions