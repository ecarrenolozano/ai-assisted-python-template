---
name: d-sync-repository-requirements
description: Synchronize approved product requirements and user stories with a remote GitHub or GitLab repository, and import triaged repository issues into product requirements for refinement. Use for the initial release when approved documentation must create repository issues, and for later product increments when triaged issues must be added to product_requirements.md, refined through Skill C, and synchronized back without duplicating existing user-story issues. Also update sdlc_docs/trace_workflow.md with the current increment status, evidence, missing information, and next action.
---

# Repository Requirements Synchronization

Coordinate the boundary between product documentation and remote repository issues without turning the repository into a duplicate requirements database.

Use these canonical artifacts:

- `sdlc_docs/01_requirements/product_requirements.md`
- `sdlc_docs/trace_workflow.md`

Read [references/process-flowchart.md](references/process-flowchart.md) before operating. Use [references/trace_workflow-template.md](references/trace_workflow-template.md) when creating or updating the central workflow table.

## Core rules

1. Treat `product_requirements.md` as the canonical source for refined requirements, user stories, acceptance criteria, and approval.
2. Treat the remote repository as the operational source for issue discussion, assignment, implementation, and issue state.
3. Process only repository issues that have passed triage.
4. Never silently approve an imported requirement.
5. Never duplicate an existing issue that already represents a user story.
6. Reuse a broad original issue as a requirement container only when multiple new user stories must be created beneath it.
7. When a broad issue produces only one user story, refine and reuse the original issue as that story; do not create a parent issue.
8. Do not create a repository issue solely to mirror a documentary requirement.
9. Do not rewrite the meaning of an approved requirement. Add a new requirement for a later increment.
10. Preserve repository issue identity, discussion, author, and history whenever an existing issue is refined.
11. Require explicit user authorization before creating, editing, closing, labeling, or linking remote issues.
12. Update only the relevant row in `trace_workflow.md`; do not duplicate requirement or issue details there.

## Inputs

### Initial release

Require:

- An approved `product_requirements.md` produced by Skill C.
- Repository identification and available repository connector, CLI, or API.
- Authorization to create or edit issues.

### Product increment

Require:

- Current `product_requirements.md`.
- One or more remote issues that have passed triage.
- Repository identification and available repository connector, CLI, or API.
- Authorization before remote write operations.

A triaged issue must contain an explicit repository signal recognized by the project, such as an approved triage label, project field, or provided issue list. Do not invent the signal.

## Outputs

Depending on the branch, produce or update:

- Remote issues and sub-issues.
- `product_requirements.md` with imported issue references or synchronized repository links.
- `trace_workflow.md` with one foundation or increment row.
- A concise synchronization summary listing actions completed, skipped, blocked, and requiring approval.

## Classification

Classify each triaged issue as one of:

- `Existing user story`
- `Broad product request`
- `Bug`
- `Technical task`
- `Duplicate`
- `Question or support request`
- `Out of scope`

Only `Existing user story` and `Broad product request` enter the requirement-refinement path.

Do not force bugs, technical tasks, duplicates, or support questions into `REQ → US` form. Link them to an existing requirement or story when evidence supports the relationship.

## Initial release behavior

For every approved requirement:

- When it has multiple user stories, create one parent issue for the requirement and one sub-issue for each story.
- When it has exactly one user story, create only one issue for the user story unless the user explicitly requests a parent issue.
- Put acceptance criteria in the user-story issue body.
- Add documentary identifiers and links without copying the whole requirements document.
- Write the created issue references back to `product_requirements.md`.

## Product increment behavior

For every triaged issue:

### Existing user story

1. Preserve the original issue.
2. Import it into `product_requirements.md` as a new unapproved requirement containing that user story.
3. Mark the story reference as the original issue.
4. Stop repository synchronization and direct the user to run Skill C for interview, refinement, acceptance criteria, and approval.
5. After Skill C approval, update the same original issue with the refined title, story, acceptance criteria, and documentary traceability.
6. Do not create a requirement issue or duplicate story issue.

### Broad product request

1. Preserve the original issue.
2. Import it into `product_requirements.md` as a new unapproved requirement.
3. Stop repository synchronization and direct the user to run Skill C.
4. After Skill C approval:
   - If Skill C produced multiple stories, reuse the original issue as the requirement container and create missing story sub-issues.
   - If Skill C produced one story, refine the original issue as that story and do not create a parent issue.
5. Write the final issue references back to `product_requirements.md`.

## Approval boundaries

Remote reading may occur when access is available. Before any write operation, present the exact proposed actions, including:

- Issues to create.
- Existing issues to edit.
- Parent/sub-issue links to establish.
- Documentary links to add.

Perform only the actions explicitly authorized by the user.

Skill D does not approve product requirements. Skill C owns requirement and story refinement and approval.

## Trace workflow update

Always use the filename:

` sdlc_docs/trace_workflow.md `

Remove the spaces shown above when using the actual path.

Keep one table with these columns:

| Item | Type | Status | Current activity | Evidence | Missing or blocked | Next action |
|---|---|---|---|---|---|---|

Use foundation rows for the initial project and release. Use one row per active increment after the first release.

Allowed status values:

- `Not Started`
- `In Progress`
- `Blocked`
- `Complete`
- `Dropped`

Typical current activities for this skill:

- `Repository Preparation`
- `Issue Import`
- `Requirements Refinement`
- `Repository Synchronization`
- `Ready for Implementation`

Examples:

- After importing a triaged issue: `In Progress | Requirements Refinement | Run Skill C`.
- After approved stories are synchronized: `Complete | Ready for Implementation | Assign or self-assign issue`.
- When remote access or authorization is missing: `Blocked | Repository Synchronization | Provide access or authorize writes`.

## Required checks

Before completing:

- Confirm the workflow branch used.
- Confirm every processed issue passed triage.
- Confirm no existing user-story issue was duplicated.
- Confirm broad single-story issues were not given unnecessary parent issues.
- Confirm imported requirements remain unapproved until Skill C approves them.
- Confirm remote writes were authorized.
- Confirm repository links and documentary IDs agree.
- Confirm `trace_workflow.md` identifies what is missing and the next action.

## Golden examples

Consult the matching example:

- Initial release: [references/golden-example/initial-release](references/golden-example/initial-release)
- Broad increment issue: [references/golden-example/increment-broad-issue](references/golden-example/increment-broad-issue)
- Existing user-story issue: [references/golden-example/increment-user-story](references/golden-example/increment-user-story)
