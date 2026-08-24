# SELL-A: Software Engineering Lifecycle enhanced LLM-based API orchestration



> **SELL-A** is a software-engineering-enhanced framework that orchestrates RESTful APIs via Large Language Models (LLMs) to fulfill user requirements expressed in natural language. It injects classical software-engineering practices —task planning, modular code generation, and tiered repair (design-level vs. code-level) — into the LLM-driven API-orchestration pipeline.

---

## 1. Highlights

- **Hierarchical API retrieval → task planning → pseudocode → executable code.** A four-stage forward pipeline that converts a natural-language request into runnable Python that invokes REST APIs.
- **Two-tier self-repair loop.**
  - *Design-level repair*: regenerates the pseudocode when a logical/plan-level error is detected.
  - *Code-level repair*: fixes the generated code when a runtime/syntactic error is detected.
  - Repairs are budgeted and tracked; an explicit `error_judge` decides which tier to invoke.
- **API calling as black-box wrappers.** Generated business code only invokes the pre-defined API functions under `Tools/`, never writes raw `requests` calls.
- **Robust LLM-output parsing.** Tolerant JSON / code-block extraction (balanced-brace aware, escape-safe) so that a single malformed LLM reply does not abort the run.

---



## 2. The SELL-A Pipeline

For each user requirement, the `SEFramework` (see [`approach/SE_Enhanced_framework.py`](approach/SE_Enhanced_framework.py)) executes the following stages:

| Step | Module                             | Purpose                                                                 |
|----:|------------------------------------|-------------------------------------------------------------------------|
|  1  | `task_plan`                        | Decompose the requirement into sub-tasks; assign a **Primary API** and **Alternative APIs** per step. |
|  2  | `pseudocode_from_plan`             | Generate Python-like pseudocode from the plan (re-issued under *design-level repair*). |
|  3  | `pseudocode_compiler`              | Compile pseudocode + API calling code into runnable Python.            |
|  4  | `code_run`                         | Execute the code in a sandboxed `subprocess`.                           |
|  5  | `error_judge`                      | Classify the failure as `design_level` or `code_level`.                |
|  6  | `code_repair` (code-level) **or**   | Fix the runnable code or, if escalated, re-do the pseudocode (design). |
|  —  | `SE_framework` (outer loop)        | Coordinates retries; total repair budget is enforced.                  |

The outer loop is bounded by `max_design_retries` and `max_total_repairs` (default: 2 each) to avoid runaway cost.

---

## 3. Installation

### 3.1 Requirements

- Python **3.10+**
- A DeepSeek account (default LLM) **or** OpenAI-compatible endpoint
- A RapidAPI key for the live tool calls in `Tools/`

### 3.2 Setup

```bash
# (Recommended) create a fresh virtual environment
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate

pip install -U pandas numpy openai httpx tiktoken
```

### 3.3 Configure credentials

Edit [`config.py`](config.py) and fill in your keys:

```python
class Config:
    openai_api_key   = '<YOUR_OPENAI_KEY>'        # for embeddings
    deepseek_key     = '<YOUR_DEEPSEEK_KEY>'      # default LLM
    Rapid_API_key    = '<YOUR_RAPIDAPI_KEY>'      # for live tool calls
    nvidia_url       = '<NVIDIA_BASE_URL>'        # optional
    nvidia_api_key   = '<NVIDIA_API_KEY>'         # optional
    react_model      = '<MODEL_NAME>'             # e.g. deepseek-chat
    react_max_turn   = 20
    tool_nums        = 3                          # top-k tool retrieval
    api_path         = os.path.join(BASE_DIR, "data", "apis.csv")
    tool_path        = os.path.join(BASE_DIR, "data", "tools.csv")
```

You may also export the corresponding environment variables; they will be picked up at runtime.

---

## 4. Running the Framework

The entry point is `SEFramework.SE_framework(user_requirement)`. A minimal end-to-end example is provided at the bottom of [`approach/SE_Enhanced_framework.py`](approach/SE_Enhanced_framework.py#L526-L571).

```python
from approach.SE_Enhanced_framework import SEFramework

se = SEFramework()
user_requirement = (
    "movies that fit params like 'Adventure' or 'Animation'. They are looking for three "
)
result = se.SE_framework(user_requirement)
print(result)
```

The generated executable script is written to `temp_output/executable_code.py` for inspection.



---
