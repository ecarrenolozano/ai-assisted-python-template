---
name: a-clarify-project-request
description: Analyze an informal request for a new software project and create, update, or review a concise Clarified Project Request. Use when the input is an email, document, meeting note, transcript, or self-authored idea that is not yet clear enough to form a Project Context. Preserve the original source, draft an initial understanding, identify no more than 10 project-level uncertainties, record stakeholder answers and their impact, keep the summary synchronized, detect contradictions, manage the document state, and prepare the document for formal human readiness approval. Do not generate the Project Context, detailed requirements, user stories, architecture, implementation plans, or approval decisions.
---

# A - Clarify Project Request

## Purpose

Transform an informal software-project request into a concise, traceable, and human-approved input for the downstream Project Context Formation skill.

Act as a requirements analyst and inception facilitator. Create, update, and review the document, but never act as its approver.

## Operating Modes

Select the mode from the user's request and available files.

### Draft

Use when an informal request is provided and `sdlc_docs/00_inception/clarified_project_request.md` does not exist.

- Create the document from `references/clarified-project-request-template.md`.
- Set `Document state` to `Draft`, then to `Under Clarification` after questions are created.
- Complete the source metadata.
- Draft the `Initial Understanding` summary.
- Generate only the project-level questions needed to reduce material uncertainty.
- Leave unanswered questions as `Open`.
- Leave the readiness approval section unapproved.

### Update

Use when `clarified_project_request.md` already exists and new answers or source material are provided.

Update the same document. Never replace it with a blank template.

- Record each answer below its matching question.
- Record who answered.
- Describe what the answer confirms, changes, or excludes.
- Update the `Initial Understanding` summary after every meaningful clarification round.
- Remove resolved uncertainty language.
- Keep unresolved questions marked `Open`.
- Keep `Document state` as `Under Clarification` while blocking uncertainties remain.
- Detect contradictions instead of resolving them silently.

### Review

Use when the document is being prepared for human approval.

- Verify that the summary reflects all confirmed answers.
- Verify that answered questions include an impact statement.
- Keep unresolved questions visible.
- Identify unsupported claims, contradictions, stale summary content, and premature technical detail.
- Remove unused placeholders.
- If no blocking uncertainty remains, set `Document state` to `Pending Approval`.
- Recommend corrections, but do not select `Ready` or `Not Ready`, enter an approver's identity, or approve the document.

## Required Inputs

Use the available combination of:

- The original informal request.
- The current `sdlc_docs/00_inception/clarified_project_request.md`, when updating or reviewing.
- New stakeholder answers, emails, notes, or corrections.

Preserve the original request as an independent source file or source reference. Do not overwrite it.

## Workflow

1. Receive the informal project request.
2. Preserve the original request as an independent source file.
3. Check whether `clarified_project_request.md` already exists in `sdlc_docs/00_inception/`.
4. If the document does not exist, create it from the bundled template and set `Document state` to `Draft`.
5. If the document already exists, load it and continue from its current state.
6. Read and analyze the original source.
7. Draft or update the `Initial Understanding` summary.
8. Identify uncertainties that could materially change the Project Context.
9. Create or update no more than 10 project-level critical questions.
10. Set `Document state` to `Under Clarification` while critical questions remain unanswered or blocking uncertainty remains.
11. If answers are not yet available, deliver the document to the requester or relevant stakeholders for clarification.
12. When answers are provided, record each answer directly below its corresponding question.
13. Describe what each answer confirms, changes, or excludes in the `Impact` field.
14. Update the `Initial Understanding` summary using the confirmed clarifications.
15. Check the document for contradictions, unsupported claims, stale summary content, and premature technical details.
16. If blocking uncertainties remain, keep `Document state` as `Under Clarification`, retain or update the open questions, and request additional clarification.
17. When no blocking uncertainties remain, set `Document state` to `Pending Approval` and submit the document to the authorized approver.
18. The authorized approver selects `Ready` or `Not Ready` in the `Readiness Approval` section and records their name, role, approval date, and any blocking issues.
19. After the approval decision is recorded, set `Document state` to `Closed`.
20. Deliver the approved Clarified Project Request to the next stage only when `Ready` is selected, approver information is complete, and `Blocking Issues` is `None`.
21. Pass the approved document to the Project Context Formation skill.

Read `references/process-flowchart.md` when explaining or verifying this workflow.

## Document State Rules

Use `Document state` only for the operational state of the file:

- `Draft`: created but not yet analyzed completely.
- `Under Clarification`: questions are open or answers are being incorporated.
- `Pending Approval`: no blocking uncertainties remain and the document awaits a formal decision.
- `Closed`: an authorized approver selected either `Ready` or `Not Ready`.

`Document state` does not determine whether the project may advance. Only the `Readiness Approval` section acts as the formal gate.

## Critical Question Rules

- Generate no more than 10 questions.
- Do not add questions merely to reach the maximum.
- Ask only questions whose answers could materially change the Project Context.
- Keep all questions at the project level.
- Prioritize the problem or opportunity, expected outcome, users or beneficiaries, rationale, initial boundary, constraints or deadlines, project-level success, ownership or approval, material dependencies, and material risks.
- Do not ask questions already answered by the source or conversation.
- Defer detailed functional questions to requirements clarification.
- Defer technical questions to architecture and implementation planning.

Do not ask about specific frameworks, libraries, programming languages, components, database schemas, storage technologies, APIs, field-level validation, algorithms, test cases, repository structure, or deployment configuration unless the source establishes one of them as a mandatory project constraint.

Treat named technologies as proposed solutions unless the source explicitly establishes them as mandatory constraints.

## Evidence and Uncertainty Rules

Distinguish internally between:

- Directly supported information.
- Interpretation.
- Proposed solution.
- Assumption.
- Open uncertainty.
- Contradiction.

Use cautious wording for unconfirmed information. Never invent answers or silently promote interpretations to confirmed facts.

When sources conflict, keep the conflict visible and create or retain a critical question for resolution.

## Output Rules

Use the exact structure in `references/clarified-project-request-template.md` unless the user explicitly requests a compatible variation.

Keep the document concise:

- Use one current `Initial Understanding` summary.
- Use no more than 10 critical questions.
- Keep answers and impacts brief.
- Remove unused question blocks before approval review.
- Store answers directly below their questions.
- Do not create a separate clarification log.

The readiness section is a formal human gate with only `Ready` and `Not Ready` states.

Never:

- Mark the document `Ready` or `Not Ready` on behalf of the approver.
- Invent the approver's name, role, or date.
- Set `Document state` to `Closed` before a human approval decision is recorded.
- Generate the downstream Project Context in the same operation unless the user explicitly invokes a separate downstream skill after approval.

## Golden Example

Use the shared TODO-board project as the canonical example for this workflow.

- Informal input: `references/in-informal-request.md`
- Expected final Clarified Project Request: `references/out-approved-clarified-project-request.md`

The Golden Example contains fictional clarification and approval data to demonstrate the expected final state. During real execution, never invent stakeholder answers or approval information.

Use the Golden Example to check boundaries, concision, question quality, state transitions, uncertainty handling, approval gating, and output structure. Do not copy its project-specific facts into unrelated requests.
