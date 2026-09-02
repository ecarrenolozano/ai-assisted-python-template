# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Development approach

This repository follows an AI-assisted, documentation-driven software development lifecycle. AI may support analysis, planning, implementation, testing, and documentation, but designated artifacts require human approval before work proceeds to the next stage.

Start with:

1. `sdlc_docs/trace_workflow.md` to see workflow status and next action.
2. `sdlc_docs/00_inception/sources/` to store original project request evidence.
3. `sdlc_docs/00_inception/project_context.md` after request clarification and approval.

Consult `WORKFLOW.md` for the complete staged sequence and skill ownership.

The AI SDLC Agent Skills are installed under:

```text
.agents/skills/
```

They are maintained separately in:

```text
https://github.com/ecarrenolozano/ai-sdlc-skills
```

## Requirements

This project uses the `skills` CLI through `npx` to manage Agent Skills.

Verify that Node.js/npm is installed:

```bash
npx --version
```

If `npx` is not available, install Node.js/npm before updating the skills.

## Setup

```bash
uv sync --all-groups
uv run pre-commit install
```

## Updating Agent Skills

To update the AI SDLC workflow skills, run from the project root:

```bash
npx skills update
```

You do not need to regenerate this project when the central skills repository changes.

To inspect the installed skills:

```bash
ls .agents/skills
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
- **Agent skills:** `.agents/skills/`
- **Author:** {{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>
- **License:** {{ cookiecutter.license }}
