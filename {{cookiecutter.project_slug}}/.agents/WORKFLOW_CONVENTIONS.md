# AI-Assisted SDLC Workflow Conventions

## Canonical stages and artifacts

1. `a-project-context-interpretation` reads `sdlc_docs/00_project_context/project_context.md`.
2. `b-requirements-clarifier` processes batches in `sdlc_docs/01_requirements/00_raw_ideas.md`.
3. `c-create-user-stories` creates `01_user_stories.md` and `02_traceability_matrix.md`.
4. `d-user-story-readiness` creates `03_user_story_readiness.md`.
5. `e-architecture-and-design` creates architecture artifacts under `02_architecture/`.
6. `f-user-story-technical-readiness` creates `04_technical_readiness.md`.
7. `g-create-repository-issues` creates `05_repository_issue_preview.md` and, after publication, `06_repository_issue_manifest.md`.
8. `h-implementation-planning` creates implementation plans under `03_implementation/`.
9. `i-testing` creates `00_testing_strategy.md`, `01_test_traceability.md`, and `02_testing_results.md` when tests run.
10. `j-validation-and-acceptance` creates `00_validation_plan.md` and `01_acceptance_results.md`.
11. `k-deployment-preparation` creates `00_deployment_plan.md`, `01_release_checklist.md`, and optionally `02_rollback_plan.md`.

## Approval rule

A document's existence is not approval. Approval records must include reviewer, decision, date, and comments. Downstream stages must honor the preceding gate.
