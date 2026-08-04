---
name: b-form-project-context
description: Transform an approved Clarified Project Request into a concise, approved Project Context for a software project. Use after a-clarify-project-request when sdlc_docs/00_inception/clarified_project_request.md is Closed, Ready, fully approved, and has no blocking issues. Create or update sdlc_docs/00_inception/project_context.md; define the problem, purpose, goal, users, high-level scope, MVP boundary, constraints, assumptions, dependencies, risks, success criteria, and confirmed responsibilities without creating detailed requirements, user stories, architecture, implementation plans, or test plans.
---

# B — Form Project Context

## Purpose

Convert an approved `Clarified Project Request` into the official high-level definition of a software project.

Produce a concise `project_context.md` that explains:

- What problem the project addresses.
- What result the project should create.
- Who will use or review the result.
- What the first useful software version includes and excludes.
- Which confirmed limits, dependencies, and risks affect the work.
- How a person will decide that the project context is ready for user-story definition.

Do not generate detailed requirements, user stories, acceptance criteria, architecture, implementation plans, or test plans.

## Required Input

Use this file as the primary input:

```text
sdlc_docs/00_inception/clarified_project_request.md
```

Proceed only when all conditions are satisfied:

- `Document state` is `Closed`.
- `Ready` is selected in the approval section.
- The approver name, role, and date are present.
- `Blocking Issues` is `None`.

If any condition is not satisfied, stop and state exactly which condition failed.

Use the original informal request only as supporting evidence. Do not restart the clarification process from the original request.

## Output

Create or update:

```text
sdlc_docs/00_inception/project_context.md
```

Use `references/project-context-template.md`.

## Operating Modes

### Draft

Use when `project_context.md` does not exist.

- Create the document from the bundled template.
- Set `Document state` to `Draft`.
- Populate only information supported by the approved source.
- Mark unsupported sections as `Not identified in the approved source` rather than inventing content.

### Update

Use when `project_context.md` already exists, answers are provided, or a reviewer selects `Not Ready`.

- Preserve confirmed information.
- Address open questions or review feedback.
- Update every affected section.
- Remove stale or contradictory statements.
- Prepare the document for a new approval cycle when needed.

### Review

Use before human approval.

- Check completeness and internal consistency.
- Check that every factual statement is traceable to the approved source or a recorded answer.
- Check alignment among the problem, goal, scope, MVP boundary, constraints, and success criteria.
- Remove temporary Working Questions after their answers have been integrated.
- Remove unnecessary repetition.
- Do not select `Ready for User Stories` or complete approval fields.

## Workflow

1. Receive the approved `clarified_project_request.md`.
2. Verify its approval gate. If invalid, stop and report the failed conditions.
3. Check whether `project_context.md` exists in `sdlc_docs/00_inception/`.
4. If it does not exist, create it from the bundled template and set `Document state` to `Draft`; otherwise, load it and continue from its current state.
5. Extract only confirmed project-level information from the approved source.
6. Draft or update Sections 2 through 17 of the Project Context.
7. For any section not supported by the source, write `Not identified in the approved source` unless the missing information blocks a coherent or approvable Project Context.
8. Check whether essential project-level information is missing, contradictory, or insufficiently precise.
9. If essential information is missing:
   - Create or update no more than 20 temporary Working Questions.
   - Do not repeat questions already answered in the approved Clarified Project Request.
   - Set `Document state` to `Under Clarification`.
   - Request answers from the person who can provide or confirm the information.
   - Record each answer and its impact.
   - Update all affected sections.
   - Return to Step 8.
10. When no essential information is missing, review the document for unsupported claims, contradictions, stale content, unnecessary repetition, scope inconsistencies, and premature technical detail.
11. If blocking issues are found, set or keep `Document state` as `Under Clarification`, add or update temporary questions or revision items, resolve them, and return to Step 8.
12. When no blocking issues remain, remove the temporary Working Questions section, set `Document state` to `Pending Approval`, and submit the document to the authorized human reviewer.
13. The reviewer selects `Ready for User Stories` or `Not Ready` and records their name, role, date, and blocking issues or feedback.
14. If `Not Ready` is selected:
   - Keep the document open.
   - Set `Document state` to `Under Clarification`.
   - Treat the feedback as required revisions.
   - Clear the current approval selection and approval fields before resubmission while preserving the prior decision in version control.
   - Return to Step 6.
15. If `Ready for User Stories` is selected, reviewer information is complete, and `Blocking Issues or Feedback` is `None`, set `Document state` to `Closed`.
16. Deliver the approved Project Context as the input to the user-story definition stage.

## Document State Rules

- `Draft`: created but not yet fully analyzed.
- `Under Clarification`: information, revisions, or review feedback still requires resolution.
- `Pending Approval`: no known blocking issue remains and a human decision is pending.
- `Closed`: a human selected `Ready for User Stories`, reviewer information is complete, and `Blocking Issues or Feedback` is `None`.

`Not Ready` is not a document state and is not terminal. It returns the document to `Under Clarification`.

## Working Question Rules

Use Working Questions only when missing information prevents a coherent or approvable Project Context.

- Ask no more than 20 questions.
- Do not ask questions merely to fill every section.
- Do not repeat questions already answered in the approved source.
- Ask in plain language.
- Ask only project-level questions.
- Record each answer and explain what it confirms, changes, or excludes.
- Integrate answers into the relevant sections.
- Remove Working Questions before approval.

Do not ask about frameworks, libraries, programming languages, components, database schemas, API contracts, field-level behavior, algorithms, repository structure, deployment configuration, or test cases unless one is already a confirmed project constraint.

## MVP Boundary Rules

In this skill, `MVP boundary` means the smallest/cheapest useful software scope approved for the first version of the project.

Define only:

- The intended user.
- The minimum useful outcome.
- The high-level capabilities needed for that outcome.
- Explicit exclusions.
- Confirmed delivery limits.
- A completion condition that can be checked from the delivered software.

Do not discuss hypotheses, experiments, pivoting, persevering, market validation, business strategy, or product research.

Do not decompose the MVP into user stories, tasks, detailed behavior, or technical components.

## Plain-Language Rules

Write for a developer who may not know Scrum, Agile, product management, or business terminology.

- Prefer concrete descriptions over role labels.
- Do not invent titles such as `Delivery Lead`, `Product Manager`, or `Sponsor`.
- Record a named responsibility only when the approved source or a recorded answer confirms it.
- When a responsibility is unknown, write `Not assigned in the approved source`.
- One person may have several confirmed responsibilities; list what the person does instead of assigning a new title.
- Use `people involved` instead of `stakeholders` when possible.
- Use `person who approves the document` instead of specialized governance terminology when possible.
- Briefly explain unavoidable terms inside the template.

## Evidence Rules

- Treat the approved Clarified Project Request as the primary evidence.
- Every factual statement must be traceable to the source or a recorded answer.
- Do not invent availability, feasibility, security conditions, resources, responsibilities, dependencies, or risks.
- Do not convert absence of information into a confirmed negative statement.
- Write `Not identified in the approved source` when relevant information is absent but not blocking.
- Clearly label assumptions as unconfirmed statements that require monitoring or later confirmation.
- Treat mentioned technologies as proposed solutions unless confirmed as mandatory limits.

## Human Approval Boundary

The skill may draft, update, and review the Project Context.

The skill must never:

- Select `Ready for User Stories` or `Not Ready` for a human.
- Invent reviewer information.
- Invent answers.
- Set `Blocking Issues or Feedback` to `None` without supporting evidence.
- Treat an AI review as formal approval.

The Golden Example contains fictional approval data only to demonstrate the expected final state.

## References

- Use `references/project-context-template.md` when creating the document.
- Use `references/process-flowchart.md` as the exact visual mirror of the workflow.
- Use `references/golden-example/in-approved-clarified-project-request.md` as the Golden Input.
- Use `references/golden-example/out-approved-project-context.md` as the Golden Output.
