# Product Requirements

## 2. Requirements Overview

| Requirement | Requirement status | Stories | Story status | Source | Repository issues |
|---|---|---|---|---|---|
| REQ-0001 Manage tasks | Approved | US-0001 | Approved | Initial Project Context | #20 Open |
| REQ-0004 Export tasks | Approved | US-0005 | Approved | Issue #84 | REQ #84 Open; US not created |

## 3. Requirements

## REQ-0004 — Export tasks

- **Status:** Approved
- **Source:** Issue #84, classified as `broad-request`
- **Repository issue:** #84 Open
- **Description:** The user must be able to export the current task list as a CSV file containing title and status.
- **Approved by:** Product requester
- **Approval date:** 2026-07-22

### US-0005 — Export tasks as CSV

- **Status:** Approved
- **Repository issue:** Not created

As a task-board user,  
I want to export my tasks as CSV,  
so that I can use the task list outside the application.

#### Acceptance Criteria

**Scenario: Export current tasks**

Given the board contains tasks  
When the user exports the board  
Then a CSV file is downloaded  
And it contains each task title and current status

## 4. Approval Record

| Requirement | Decision | Approved by | Date |
|---|---|---|---|
| REQ-0004 | Approved | Product requester | 2026-07-22 |
