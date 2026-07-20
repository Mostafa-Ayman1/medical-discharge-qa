# 🏥 Medical Discharge QA System

An AI-powered application that generates, evaluates, and automatically improves post-operative discharge instructions using the **Evaluator-Optimizer** design pattern.

Instead of generating instructions only once, the system performs an iterative quality assurance loop until the instructions satisfy predefined medical quality criteria or the maximum number of iterations is reached.

---

## ✨ Features

* Generate patient-friendly discharge instructions for surgical procedures.
* Evaluate instructions using a dedicated AI Quality Assurance agent.
* Automatically improve instructions based on evaluator feedback.
* Repeat the evaluation-improvement cycle until approval.
* Clean Gradio user interface.
* Modular agent-based architecture.
* Built to demonstrate the **Evaluator-Optimizer** pattern from Agentic AI.

---

## 🧠 Design Pattern

This project implements the **Evaluator-Optimizer** pattern.

```text
                 User
                   │
                   ▼
            Generator Agent
                   │
                   ▼
     Discharge Instructions
                   │
                   ▼
            Evaluator Agent
             PASS / FAIL
              │        │
              │        ▼
              │   Feedback
              │        │
              ▼        ▼
          Final Output Optimizer Agent
                        │
                        ▼
              Improved Instructions
                        │
                        └──────────────► Evaluator
```

The system continues improving the instructions until:

* ✅ The evaluator returns **PASS**
* 🔁 The maximum number of optimization iterations is reached

---

## 📂 Project Structure

```text
medical-discharge-qa/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── agents/
│   ├── orchestrator.py
│   ├── generator.py
│   ├── evaluator.py
│   └── optimizer.py
│
├── prompts/
│   ├── generator.txt
│   ├── evaluator.txt
│   └── optimizer.txt
│
├── services/
│   └── openai_client.py
│
├── ui/
│   └── gradio.py.py
│
└── utils/
    ├── helpers.py
    └── logger.py
```

---

## ⚙️ Workflow

1. The user enters a surgical procedure.
2. The **Generator Agent** creates discharge instructions.
3. The **Evaluator Agent** reviews the instructions against predefined quality rules.
4. If the evaluation passes, the instructions are returned.
5. If the evaluation fails, feedback is sent to the **Optimizer Agent**.
6. The **Optimizer Agent** improves the instructions.
7. The evaluation loop repeats until approval or the maximum number of iterations is reached.

---

## 🏥 Evaluation Criteria

The Evaluator checks whether the instructions:

* Use clear, patient-friendly language.
* Include essential post-operative care guidance.
* Mention warning signs requiring medical attention.
* Include follow-up recommendations.
* Avoid unsafe or misleading medical advice.
* Maintain a supportive and professional tone.

---

## 🛠️ Technologies

* Python
* OpenAI API
* Gradio
---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/medical-discharge-qa.git
cd medical-discharge-qa
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

Run the application:

```bash
python app.py
```

---

## 🎯 Learning Objectives

This project demonstrates how to:

* Build AI systems using the **Evaluator-Optimizer** pattern.
* Separate generation, evaluation, and optimization into independent agents.
* Design iterative AI workflows.
* Improve output quality through structured feedback loops.
* Create maintainable agent-based applications.

---
