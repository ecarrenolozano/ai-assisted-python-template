---
name: c-manage-product-requirements
description: Create and maintain a single canonical product requirements document with a hierarchy of requirements and user stories. Use for the initial release when converting an approved project context into requirements, user stories, and acceptance criteria, and for later increments when triaged repository issues have already been imported as unapproved requirements. Refine only blocking gaps through chat, preserve approved requirements, create new requirements for later changes, support existing repository issues without duplicating user-story issues, prepare human approval, and maintain minimal repository traceability.
---

# Manage Product Requirements

Maintain one canonical file:

` sdlc_docs/01_requirements/product_requirements.md `

Use a two-level hierarchy:

```text
REQ
└── one or more US
```

Keep acceptance criteria inside each user story. Do not create acceptance-criterion issues.

## Required inputs

Choose one mode.

### Initial release

Require:

- an approved `sdlc_docs/00_inception/project_context.md`

Create:

- `sdlc_docs/01_requirements/product_requirements.md`

### Product increment

Require:

- the current `sdlc_docs/01_requirements/product_requirements.md`
- one or more triaged repository issues already imported into the document as unapproved requirements
- the issue classification for each imported item:
  - `broad-request`
  - `user-story`

Do not read or modify the remote repository directly. A repository synchronization skill performs that work before and after this skill.

## Core rules

1. Treat an approved requirement as immutable.
2. Create a new requirement for every later approved product change.
3. Preserve an approved requirement's original description, stories, criteria, and approval record.
4. Allow one requirement to contain one or more user stories.
5. Split by independently observable user outcomes, never by technical layers or implementation tasks.
6. Ask only questions whose answers are necessary to produce meaningful stories or acceptance criteria.
7. Conduct clarification and approval through chat.
8. Consolidate decisions into the document; do not copy the interview transcript.
9. Never approve on the user's behalf.
10. Never duplicate an existing repository issue that already represents a user story.
11. Use a broad existing issue as a repository container only when it must hold newly created user-story sub-issues.
12. Keep contributor assignment, labels, milestones, implementation discussion, and pull requests in the repository.

## Minimal statuses

Requirement statuses:

- `Unapproved`
- `Under Clarification`
- `Pending Approval`
- `Approved`
- `Retired`

User story statuses:

- `Draft`
- `Pending Approval`
- `Approved`
- `Retired`

Repository state recorded in the document:

- `Not created`
- `Open`
- `Closed`

## Workflow

Follow [process-flowchart.md](references/process-flowchart.md). It contains two explicit entry branches: `initial release` and `product increment`. The branches must remain visible in both the written workflow and the Mermaid flowchart, and both representations are normative and must remain synchronized.

## Output format

Follow [product-requirements-template.md](references/product-requirements-template.md).

Keep these sections only:

1. Document Control
2. Requirements Overview
3. Requirements
4. Approval Record

## Initial release behavior

1. Read the approved Project Context.
2. Extract product requirements for the first release.
3. Ask blocking clarification questions.
4. Generate one or more user stories under each requirement.
5. Add observable acceptance criteria using Given/When/Then when suitable.
6. Present each requirement and its stories for chat review.
7. Mark approved items as `Approved` and update the overview table.
8. Leave repository links as `Not created` for the synchronization skill to create later.

## Increment behavior

Process only imported requirements with status `Unapproved` or `Under Clarification`.

### Imported broad request

When the source issue is classified as `broad-request`:

- keep the imported requirement
- clarify only blocking gaps
- generate one or more user stories
- preserve the source issue as the future repository container
- mark each generated story's repository issue as `Not created`

After approval, the synchronization skill may refine the original issue as the requirement container and create missing user-story sub-issues.

### Imported user story

When the source issue is classified as `user-story`:

- keep the imported requirement as a documentation-only grouping
- refine the existing story through chat
- preserve the original issue as that story's repository issue
- do not request or propose a separate requirement issue
- do not create a duplicate story

After approval, the synchronization skill updates the original issue with the refined story and acceptance criteria.

## Review and approval

Review one requirement at a time unless the user asks for batch review.

Before requesting approval, show:

- requirement title and description
- its user stories
- acceptance criteria
- source issue and intended repository action

Accept either:

- `Approved`
- concrete corrections

On corrections:

- keep the requirement `Under Clarification`
- revise only affected content
- present it again

On approval:

- mark the requirement and reviewed stories `Approved`
- record approver and date
- update the overview table

## Traceability

Maintain one compact table at the start of the document:

| Requirement | Requirement status | Stories | Story status | Source | Repository issues |

Use the requirement detail to store exact issue references.

For a broad issue:

- requirement source issue: original issue
- requirement repository issue: original issue
- generated stories: `Not created` until synchronized

For an issue that already is a story:

- requirement source: original issue
- requirement repository issue: `None — documentation only`
- story repository issue: original issue

Do not mirror repository activity beyond issue identity and `Open` or `Closed` state.

## Quality checks

Before saving:

- ensure every `US` is nested under exactly one primary `REQ`
- ensure IDs are unique and never reused
- ensure approved content was not rewritten
- ensure each story describes a user-observable outcome
- ensure each story has testable acceptance criteria
- ensure imported user-story issues were reused, not duplicated
- ensure the overview table matches the detailed sections
- ensure unresolved blocking questions prevent approval

## Golden examples

Use these examples to demonstrate the behavioral contract:

- [Initial release](references/golden-example/initial-release/)
- [Increment from a broad issue](references/golden-example/increment-broad-issue/)
- [Increment from an existing user-story issue](references/golden-example/increment-user-story/)
