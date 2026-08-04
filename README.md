# AI-Assisted Python Project Template

A Cookiecutter template for Python applications and libraries developed through a documentation-driven, approval-gated, AI-assisted software development lifecycle.

## Generate a project

```bash
uvx cookiecutter path/to/ai-assisted-python-template
```

The generated repository includes:

- `src/` package layout with Hatchling;
- `uv`, pytest, Ruff, mypy, coverage, and pre-commit configuration;
- reusable AI skills under `.agents/skills/`;
- staged SDLC documentation under `sdlc_docs/`;
- approval gates for human-controlled transitions;
- documentation placeholders for MkDocs or Zensical;
- platform-neutral issue and change-request templates.

## Template scope

The template provides the reusable process and infrastructure. Project-specific requirements, architecture, code, datasets, and exercises are added after generation.
