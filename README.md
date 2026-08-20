<img src="assets/branding/logo-horizontal-1600x400.png" alt="AI SDLC Python Template logo" width="1100" />

# AI SDLC - Python template

A Cookiecutter template for Python applications and libraries built with a controlled, approval-gated, AI-assisted Software Development Life Cycle workflow.

## Why this template

This template helps teams start Python projects with:

- a reproducible repository layout;
- built-in quality tooling;
- skill-driven SDLC stages;
- human approval gates between workflow stages.

## Quick start

### 1) Install Cookiecutter

Choose one option:

```bash
uv tool install cookiecutter
```

```bash
pipx install cookiecutter
```

```bash
python -m pip install cookiecutter
```

### 2) Generate a project

```bash
cookiecutter https://github.com/ecarrenolozano/ai-assisted-python-template.git
```

### 3) Run initial checks

```bash
cd <your-project-slug>
uv sync --all-groups
uv run pre-commit install
uv run pytest
```

## Cookiecutter basics for first-time users

Cookiecutter asks for prompt values and generates a new repository from this template.

Run with prompts:

```bash
cookiecutter https://github.com/ecarrenolozano/ai-assisted-python-template.git
```
Reuse previous answers:

```bash
cookiecutter https://github.com/ecarrenolozano/ai-assisted-python-template.git --replay
```

## What you get

- `src/` package layout with Hatchling;
- `uv`, pytest, pytest-bdd, Ruff, mypy, coverage, and pre-commit configuration;
- reusable Agent Skills under a provider-aware skills folder;
- staged SDLC documentation under `sdlc_docs/`;
- workflow traceability and approval-gated transitions;
- documentation placeholders for MkDocs or Zensical;
- issue and change-request templates.

The `agent_provider` prompt controls where the generated skills are stored:

| Choice | Skills path |
|--------|-------------|
| `portable` | `.agents/skills` |
| `claude` | `.claude/skills` |
| `codex` | `.codex/skills` |
| `copilot` | `.agents/skills` |
| `gemini` | `.gemini/skills` |
| `cursor` | `.cursor/skills` |
| `other` | `.agents/skills` |

![Generated project map](assets/readme/template-workflow-map.png)

## SDLC navigation in generated projects

Start here after generation:

1. `sdlc_docs/trace_workflow.md`
2. `sdlc_docs/00_inception/sources/`
3. `WORKFLOW.md`

The generated Agent Skills folder drives stage transitions from inception through release preparation.

## Troubleshooting

- `cookiecutter: command not found`: reopen your shell, or run with `uvx cookiecutter`.
- Destination folder already exists: choose another output folder, or remove the old generated repository.
- Wrong prompt values: re-run with `--replay` or pass explicit key-value arguments.

## Template scope

This template provides reusable process and infrastructure. Project-specific requirements, architecture, code, datasets, and exercises are added after generation.


---

#### Authors

|                    |                                                            |                     |
|--------------------|------------------------------------------------------------|---------------------|
| Edwin Carreño      | [Scientific Software Center](https://www.ssc.uni-heidelberg.de/en)                  | Heidelberg, Germany |
| Maxim Scheremetjew | [Max Plank Institute of Molecular Cell Biology and Genetics](https://www.mpi-cbg.de/) | Dresden, Germany    |
