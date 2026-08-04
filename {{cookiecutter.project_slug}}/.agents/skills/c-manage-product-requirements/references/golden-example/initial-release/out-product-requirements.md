# Product Requirements

## 1. Document Control

- **Project:** Personal Task Board
- **Source project context:** `sdlc_docs/00_inception/project_context.md`
- **Last updated:** 2026-07-22

## 2. Requirements Overview

| Requirement | Requirement status | Stories | Story status | Source | Repository issues |
|---|---|---|---|---|---|
| REQ-0001 Manage tasks | Approved | US-0001, US-0002 | Approved | Initial Project Context | Not created |
| REQ-0002 Organize tasks by status | Approved | US-0003 | Approved | Initial Project Context | Not created |
| REQ-0003 Preserve the board | Approved | US-0004 | Approved | Initial Project Context | Not created |

## 3. Requirements

## REQ-0001 — Manage tasks

- **Status:** Approved
- **Source:** Initial Project Context
- **Repository issue:** Not created
- **Description:** The user must be able to create and edit personal tasks.
- **Approved by:** Product requester
- **Approval date:** 2026-07-22

### US-0001 — Create a task

- **Status:** Approved
- **Repository issue:** Not created

As a task-board user,  
I want to create a task,  
so that I can record an activity.

#### Acceptance Criteria

**Scenario: Create a valid task**

Given the board is available  
When the user creates a task with a title  
Then the task is added to TODO

### US-0002 — Edit a task

- **Status:** Approved
- **Repository issue:** Not created

As a task-board user,  
I want to edit a task,  
so that I can correct its information.

#### Acceptance Criteria

**Scenario: Save edited information**

Given a task exists  
When the user changes its title  
Then the updated title is shown

## REQ-0002 — Organize tasks by status

- **Status:** Approved
- **Source:** Initial Project Context
- **Repository issue:** Not created
- **Description:** The user must be able to move tasks between TODO, DOING, and DONE.
- **Approved by:** Product requester
- **Approval date:** 2026-07-22

### US-0003 — Move a task

- **Status:** Approved
- **Repository issue:** Not created

As a task-board user,  
I want to move a task between sections,  
so that its position reflects its current status.

#### Acceptance Criteria

**Scenario: Move a task**

Given a task exists in TODO  
When the user moves it to DOING  
Then it appears only in DOING

## REQ-0003 — Preserve the board

- **Status:** Approved
- **Source:** Initial Project Context
- **Repository issue:** Not created
- **Description:** The board must preserve tasks and their sections between sessions.
- **Approved by:** Product requester
- **Approval date:** 2026-07-22

### US-0004 — Restore the board

- **Status:** Approved
- **Repository issue:** Not created

As a task-board user,  
I want my board restored when I return,  
so that I can continue my work.

#### Acceptance Criteria

**Scenario: Reopen the board**

Given tasks exist in different sections  
When the user reopens the application  
Then each task appears in its previous section

## 4. Approval Record

| Requirement | Decision | Approved by | Date |
|---|---|---|---|
| REQ-0001 | Approved | Product requester | 2026-07-22 |
| REQ-0002 | Approved | Product requester | 2026-07-22 |
| REQ-0003 | Approved | Product requester | 2026-07-22 |
