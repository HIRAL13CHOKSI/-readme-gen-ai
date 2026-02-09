# readme-gen-ai

Automated README generation system for CSE 5095.  
This project generates README files directly from single Python scripts using
Large Language Models (OpenAI and Gemini), with optional AST-based static analysis.
It also includes a fully automated evaluation pipeline for reproducible experiments.

---

## Environment Configuration

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Set API keys

This project supports **OpenAI** and **Google Gemini** models for both README
generation and evaluation.

Set the following environment variables:

#### OpenAI
```bash
export OPENAI_API_KEY=YOUR_OPENAI_KEY
```

#### Gemini (Google)
```bash
export GEMINI_API_KEY=YOUR_GEMINI_KEY
```

> At least one API key must be set to run generation or evaluation.

---

## Generate READMEs

### Generate a README for a single Python script

```bash
python -m readmegenv2 path/to/script.py \
  --out path/to/README.generated.md \
  --provider openai \
  --model gpt-4o-mini \
  --probe-help \
  --print-facts
```

---

### Generate READMEs for an entire folder

```bash
python -m readmegenv2 Sample_scripts \
  --out artifacts/generated_readmes \
  --provider auto \
  --model gpt-4o-mini
```

Each `.py` file receives its own generated README in the output directory.

---

## Running the Evaluation Workflow (AST-Grounded)

### OpenAI → OpenAI

```bash
python tests/run_readmegenv2_eval.py \
  --gen-provider openai \
  --gen-model gpt-4o-mini \
  --judge-provider openai \
  --judge-model gpt-4o-mini \
  --run-label ast-openai-openai
```

### OpenAI → Gemini

```bash
python tests/run_readmegenv2_eval.py \
  --gen-provider openai \
  --gen-model gpt-4o-mini \
  --judge-provider google \
  --judge-model gemini-2.0-flash \
  --run-label ast-openai-gemini
```

### Gemini → OpenAI

```bash
python tests/run_readmegenv2_eval.py \
  --gen-provider google \
  --gen-model gemini-2.0-flash \
  --judge-provider openai \
  --judge-model gpt-4o-mini \
  --run-label ast-gemini-openai
```

### Gemini → Gemini

```bash
python tests/run_readmegenv2_eval.py \
  --gen-provider google \
  --gen-model gemini-2.0-flash \
  --judge-provider google \
  --judge-model gemini-2.0-flash \
  --run-label ast-gemini-gemini
```

---

## LLM-Only (No-AST) Evaluation Pipeline

Outputs are written to:

```text
artifacts/readmegenv2_eval_no_ast/<run-label>/
```

### OpenAI → OpenAI

```bash
python tests/run_readmegenv2_no_ast_eval.py \
  --gen-provider openai \
  --gen-model gpt-4o-mini \
  --judge-provider openai \
  --judge-model gpt-4o-mini \
  --run-label no-ast-openai-openai
```

### OpenAI → Gemini

```bash
python tests/run_readmegenv2_no_ast_eval.py \
  --gen-provider openai \
  --gen-model gpt-4o-mini \
  --judge-provider google \
  --judge-model gemini-2.0-flash \
  --run-label no-ast-openai-gemini
```

### Gemini → OpenAI

```bash
python tests/run_readmegenv2_no_ast_eval.py \
  --gen-provider google \
  --gen-model gemini-2.0-flash \
  --judge-provider openai \
  --judge-model gpt-4o-mini \
  --run-label no-ast-gemini-openai
```

### Gemini → Gemini

```bash
python tests/run_readmegenv2_no_ast_eval.py \
  --gen-provider google \
  --gen-model gemini-2.0-flash \
  --judge-provider google \
  --judge-model gemini-2.0-flash \
  --run-label no-ast-gemini-gemini
```

---

## Reproducibility Notes

- All experiments can be reproduced by setting the appropriate API keys and
  re-running the commands above.
- AST-grounded and No-AST results are kept in separate artifact directories.
