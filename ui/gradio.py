import gradio as gr

# استخدام ثيم هادي ومناسب مع إمكانية دعم الـ Dark/Light mode
custom_theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="slate",
    font=[gr.themes.GoogleFont("Inter"), "sans-serif"],
)

# تحسين الـ CSS ليكون متوافق أكتر مع مكونات Gradio ولتجنب تعارض الألوان
CUSTOM_CSS = """

.output-box {
    padding: 20px !important;
    min-height: 280px;
    background-color: white;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-size: 15px !important;
    line-height: 1.6 !important;
}


.feedback-box {
    padding: 15px !important;
    min-height: 120px;
    background-color: #fef2f2 !important; 
    color: #ef4444 !important; 
    border: 1px solid #fecaca;
    border-radius: 8px;
}

.dark .output-box {
    background-color: #1e293b;
    border-color: #334155;
}
.dark .feedback-box {
    background-color: #450a0a !important;
    color: #fca5a5 !important;
    border-color: #7f1d1d;
}
"""

def create_ui(fn):
    with gr.Blocks(
        theme=custom_theme,
        css=CUSTOM_CSS,
        title="Medical Discharge QA System",
    ) as demo:

        gr.Markdown(
            """
            <div style="text-align: center; margin-bottom: 15px;">
                <h1>🏥 Medical Discharge QA System</h1>
                <p style="color: gray; font-size: 16px;">
                    Generate post-operative discharge instructions, automatically 
                    evaluate their quality, and improve them using the <b>Evaluator-Optimizer Pattern</b>.
                </p>
            </div>
            """
        )

        with gr.Row():

            # ---------------- Left Column (Inputs) ---------------- #
            with gr.Column(scale=1, variant="panel"):
                gr.Markdown("### ⚙️ Setup & Generation")
                
                operation_input = gr.Textbox(
                    label="Operation / Procedure",
                    placeholder="e.g. Laparoscopic Appendectomy...",
                    lines=2,
                )

                with gr.Row():
                    clear_btn = gr.ClearButton(value="🗑️ Clear", size="sm")
                    generate_btn = gr.Button("🚀 Generate & Evaluate", variant="primary", size="sm")

                gr.Markdown("---")
                gr.Examples(
                    examples=[
                        ["Laparoscopic Appendectomy"],
                        ["Cesarean Section (C-Section)"],
                        ["Cardiac Catheterization"],
                        ["Inguinal Hernia Repair"],
                    ],
                    inputs=operation_input,
                    label="Quick Examples",
                )

           # ---------------- Right Column (Outputs) ---------------- #
            with gr.Column(scale=2):
                
                status_output = gr.Markdown(
                    value="*Status: Waiting for input...*",
                )

               
                with gr.Group():
                    gr.Markdown("### 📄 Current Draft / Final Instructions")
                    instructions_output = gr.Markdown(
                        value="*The instructions will appear here...*",
                        elem_classes="output-box",
                    )

                with gr.Group():
                    gr.Markdown("### 📝 Evaluator Feedback")
                    feedback_output = gr.Markdown(
                        value="*Evaluator notes will appear here...*",
                        elem_classes="feedback-box",
                    )

        # ---------------- Event Listeners ---------------- #
        generate_btn.click(
            fn=fn,
            inputs=operation_input,
            outputs=[
                status_output,
                instructions_output,
                feedback_output,
            ],
        )

        # ربط زر المسح لتفريغ كل الخانات وإرجاع الحالة لوضعها الأصلي
        clear_btn.click(
            fn=lambda: ("", "*Status: Waiting for input...*", "", ""),
            inputs=None,
            outputs=[operation_input, status_output, instructions_output, feedback_output],
        )

    return demo

