# Golden Example — Project Context

## 1. Document Control

- **Project name:** Personal Task Board
- **Source request:** `clarified_project_request.md`
- **Prepared by:** Edwin Carreño
- **Version:** 1.0
- **Last updated:** 2026-07-22
- **Document state:** Closed

## 2. Project Summary

The Personal Task Board project will provide Robert Bosch with a browser-based application for managing personal tasks on one board with three fixed sections: `TODO`, `DOING`, and `DONE`. The first useful version must be available within one week, support creating, editing, deleting, and moving tasks, and preserve tasks after the browser is closed and reopened. The project is limited to one user and one board.

## 3. Background

Robert currently uses separate notes and memory to manage personal activities. This makes it difficult for him to see which tasks are pending, in progress, or completed. He has also reported overlooking pending tasks and losing track of work in progress.

## 4. Problem Statement

Robert does not have one persistent visual place for organizing personal tasks by status. As a result, he depends on separate notes and memory and has limited visibility into pending, active, and completed work.

## 5. Why the Project Is Needed

The current approach is already causing Robert to overlook tasks and lose track of ongoing work. He needs a simple replacement immediately, and the first useful version must be available within one week.

## 6. Desired Future Situation

Robert can open one board in a web browser and see which personal tasks are pending, in progress, or completed without relying on separate notes for the supported workflow.

## 7. Project Goal

Deliver within one week a browser-based personal task board that allows Robert Bosch to create, edit, delete, move, and retain tasks across `TODO`, `DOING`, and `DONE`.

## 8. Expected Outcomes

- Robert has one visual place for tracking personal tasks.
- Pending, in-progress, and completed tasks are clearly separated.
- Tasks remain available after the browser is closed and reopened.
- The supported workflow can be managed without separate notes.

## 9. People Involved

### Intended Users

- Robert Bosch, the only user of the first version.

### Other People Affected

- None identified in the approved source.

### Confirmed Responsibilities

- **Robert Bosch:** Requested the project, defines the intended result, makes project-level decisions, and confirms whether the delivered software meets the agreed scope.
- **Edwin Carreño:** Prepared the inception documents.

## 10. High-Level Scope

### Included

- One browser-based personal task board.
- Three fixed sections: `TODO`, `DOING`, and `DONE`.
- Creating, editing, deleting, and moving personal tasks.
- Preserving tasks between browser sessions.
- A first useful version within one week.

### Excluded

- Authentication and user accounts.
- Multiple users, shared boards, and collaboration.
- Multiple boards or configurable sections.
- Notifications, task deadlines, priorities, labels, and attachments.
- Native mobile or desktop applications.
- Team coordination and project portfolio management.

## 11. MVP Boundary

In this document, the MVP boundary is the smallest useful software scope approved for the first version. It does not include hypotheses, experiments, or business validation.

### Intended User

Robert Bosch.

### Minimum Useful Outcome

Robert can manage the supported personal task workflow on one persistent visual board instead of using separate notes and memory.

### Included High-Level Capabilities

- Create personal tasks.
- Edit personal tasks.
- Delete personal tasks.
- View tasks in `TODO`, `DOING`, and `DONE`.
- Move tasks between the three sections.
- Retain tasks after closing and reopening the browser.

### Explicitly Excluded

- Authentication and multiple users.
- Collaboration and shared boards.
- Multiple boards and configurable sections.
- Notifications and advanced task information.
- Native applications.

### Confirmed Delivery Limits

- The first useful version must be available within one week.
- The software must run in a web browser.
- The first version supports one user and one board.
- The board contains exactly three fixed sections.

### Completion Condition

The approved first-version scope is delivered when Robert can create, edit, delete, view, move, and retain personal tasks on one browser-based board with the three fixed sections.

## 12. Constraints

- The first useful version must be available within one week.
- The software must run in a web browser.
- The first version is limited to one user and one board.
- The board sections are fixed as `TODO`, `DOING`, and `DONE`.

## 13. Assumptions

- No assumptions recorded.

## 14. Dependencies

- No dependencies identified in the approved source.

## 15. Risks and Uncertainties

- **One-week deadline:** Adding capabilities outside the approved scope could prevent delivery within the confirmed deadline.
- **Detailed behavior not yet defined:** The exact behavior and acceptance conditions for creating, editing, deleting, moving, and retaining tasks must be defined during user-story creation.
- **Usability wording:** The request describes the application as simple and easy to use, but observable usability conditions have not yet been defined.

## 16. Success Criteria

- A first useful version is available within one week.
- Robert can create, edit, delete, and view personal tasks on one board.
- Robert can move tasks between `TODO`, `DOING`, and `DONE`.
- Tasks remain available after the browser is closed and reopened.
- Robert confirms that the delivered software supports the agreed personal task workflow without requiring separate notes for that workflow.

## 17. Confirmed Decisions and Responsibilities

- **Person who requested the project:** Robert Bosch
- **Person who makes project-level decisions:** Robert Bosch
- **Person who confirms the software meets the agreed scope:** Robert Bosch
- **Person responsible for building the software:** Not assigned in the approved source

## 18. Project Context Approval

### Status

- [x] Ready for User Stories
- [ ] Not Ready

### Reviewed by

- **Name:** Robert Bosch
- **Role or responsibility:** Requested the project and makes project-level decisions
- **Date:** 2026-07-22

### Blocking Issues or Feedback

None.

### Approval Rule

The document can be closed and passed to user-story definition only when:

- `Ready for User Stories` is selected.
- The reviewer name, responsibility, and date are recorded.
- `Blocking Issues or Feedback` is `None`.
