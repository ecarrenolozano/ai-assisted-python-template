# Product Requirements

## 2. Requirements Overview

| Requirement | Requirement status | Stories | Story status | Source | Repository issues |
|---|---|---|---|---|---|
| REQ-0001 Manage tasks | Approved | US-0001 | Approved | Initial Project Context | #20 Open |
| REQ-0005 Filter tasks | Approved | US-0006 | Approved | Issue #90 | US #90 Open |

## 3. Requirements

## REQ-0005 — Filter tasks

- **Status:** Approved
- **Source:** Issue #90, classified as `user-story`
- **Repository issue:** None — documentation only
- **Description:** The user must be able to limit the visible tasks to one selected priority.
- **Approved by:** Product requester
- **Approval date:** 2026-07-22

### US-0006 — Filter tasks by priority

- **Status:** Approved
- **Repository issue:** #90 Open

As a task-board user,  
I want to filter tasks by priority,  
so that I can focus on the most urgent work.

#### Acceptance Criteria

**Scenario: Select one priority**

Given tasks with different priorities exist  
When the user selects one priority  
Then only tasks with that priority are displayed

**Scenario: Clear the filter**

Given a priority filter is active  
When the user clears the filter  
Then all tasks are displayed

## 4. Approval Record

| Requirement | Decision | Approved by | Date |
|---|---|---|---|
| REQ-0005 | Approved | Product requester | 2026-07-22 |
