# AI-Assisted SDLC Workflow

The repository uses the following staged workflow:

1. Interpret and approve project context.
2. Clarify raw requirements.
3. Create and assess user stories.
4. Design and approve architecture.
5. assess technical readiness.
6. prepare repository issues.
7. plan implementation and TDD work.
8. implement and execute testing.
9. validate acceptance criteria and approve integration.
10. prepare deployment and release.

The reusable skills in `.agents/skills/` support these stages. Read `.agents/WORKFLOW_CONVENTIONS.md` for canonical artifact paths and naming conventions.

## Approval rule

Do not treat AI-generated documentation, plans, code, tests, or validation results as approved by default. A human reviewer must record a decision in each required approval gate.
