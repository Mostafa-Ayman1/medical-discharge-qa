from agents.generator import run as generator
from agents.evaluator import run as evaluator
from agents.optimizer import run as optimizer

MAX_LOOPS = 3


def run(operation: str):
    """
    Evaluator-Optimizer Loop

    1. Generate instructions.
    2. Evaluate.
    3. If PASS -> return.
    4. If FAIL -> optimize.
    5. Repeat up to MAX_LOOPS.
    """

    # Generate once
    instructions = generator(operation)

    for attempt in range(1, MAX_LOOPS + 1):

        print("=" * 60)
        print(f"🔄 Iteration {attempt}")

        evaluation = evaluator(instructions)

        # PASS
        if evaluation["status"] == "PASS":

            print("✅ Evaluation Passed")

            return {
                "status": "PASS",
                "iterations": attempt,
                "instructions": instructions
            }

        # FAIL
        print("❌ Evaluation Failed")
        print("Improving instructions...")

        instructions = optimizer(
            instructions,
            evaluation["feedback"]
        )

    # Failed after max loops
    return {
        "status": "FAIL",
        "iterations": MAX_LOOPS,
        "instructions": instructions,
        "feedback": evaluation["feedback"]
    }