import json
import config
from services.openai_client import client
from utils.helpers import load_prompt
from utils.logger import log

SYSTEM_PROMPT = load_prompt("evaluator.txt")


def run(instructions: str) -> dict:
    """
    Evaluate discharge instructions.
    """

    print("=" * 60)
    print("🔍 Evaluator Started")

    response = client.responses.create(
        model=config.OPENAI_MODEL,
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": instructions,
            },
        ],
    )

    result = json.loads(response.output_text)

    log(
        f"""
        EVALUATOR

        Instructions:

        {instructions}

        Evaluation:

        {json.dumps(result, indent=2)}
        """
    )

    print(f"Status: {result['status']}")
    print("✅ Evaluator Finished")

    return result