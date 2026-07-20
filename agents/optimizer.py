import config
from services.openai_client import client
from utils.helpers import load_prompt
from utils.logger import log

SYSTEM_PROMPT = load_prompt("optimizer.txt")


def run(instructions: str, feedback: list[str]) -> str:
    """
    Improve the discharge instructions based on evaluator feedback.
    """

    print("=" * 60)
    print("🛠️ Optimizer Started")

    feedback_text = "\n".join(f"- {item}" for item in feedback)

    response = client.responses.create(
        model=config.OPENAI_MODEL,
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": f"""
                 Current Instructions:

                {instructions}

                Evaluator Feedback:

                {feedback_text}
            """,
            },
        ],
    )

    improved = response.output_text.strip()

    log(
        f"""
        OPTIMIZER

        Original Instructions:

        {instructions}

        Feedback:

        {feedback_text}

        Improved Instructions:

        {improved}
"""
    )

    print("✅ Optimizer Finished")

    return improved