# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Development approach

This repository follows an AI-assisted, documentation-driven software development lifecycle. AI may support analysis, planning, implementation, testing, and documentation, but designated artifacts require human approval before work proceeds to the next stage.

Start with [`sdlc_docs/00_project_context/project_context.md`](sdlc_docs/00_project_context/project_context.md) and consult [`WORKFLOW.md`](WORKFLOW.md) for the complete sequence.

## Setup

```bash
uv sync --all-groups
uv run pre-commit install
```

## Quality checks

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy src
```

## Documentation

```bash
uv run {{ cookiecutter.documentation_tool }} serve
```

## Project metadata

- **Type:** {{ cookiecutter.project_type }}
- **Python:** {{ cookiecutter.python_version }}+
- **Author:** {{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>
- **License:** {{ cookiecutter.license }}
