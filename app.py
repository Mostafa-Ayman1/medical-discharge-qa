from ui.gradio import create_ui
from agents.orchestrator import run




def generate(operation):

    result = run(operation)

    if result["status"] == "PASS":

        status = f"""
                    ## ✅ Approved

                    Iterations: {result['iterations']}
                """
        feedback = "No feedback."
    else:

        status = f"""
                    ## ❌ Needs Improvement

                    Maximum iterations reached ({result['iterations']}).
                 """

        feedback = "\n".join(
            f"- {item}"
            for item in result["feedback"]
        )

    return (
        status,
        result["instructions"],
        feedback
    )

demo = create_ui(generate)

if __name__ == "__main__":
    demo.launch()