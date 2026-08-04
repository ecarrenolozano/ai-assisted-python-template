# Project Context

## How to Use This Document

This document turns an approved Clarified Project Request into a high-level definition of the software project.

Follow these steps:

1. Verify that the source request is closed, approved, and has no blocking issues.
2. Complete Section 1 and set `Document state` to `Draft` when creating the file.
3. Populate Sections 2–17 using only confirmed information.
4. When information is absent but does not block approval, write `Not identified in the approved source`.
5. Do not invent facts merely to complete a section.
6. Define the MVP boundary as the smallest useful software scope approved for the first version.
7. Use temporary Working Questions only when missing information prevents a coherent or approvable Project Context.
8. Ask no more than 10 questions and do not repeat questions already answered in the approved source.
9. Integrate answers into the affected sections and remove Working Questions before approval.
10. Set `Document state` to `Pending Approval` only when no blocking issue remains.
11. If the reviewer selects `Not Ready`, set `Document state` to `Under Clarification`, address the feedback, and resubmit.
12. Set `Document state` to `Closed` only after valid human approval as `Ready for User Stories`.

### Editing Rules

- Use short paragraphs and direct statements.
- Use plain language that does not require knowledge of Scrum, Agile, or business terminology.
- Do not assign titles or responsibilities that are not confirmed.
- Do not present assumptions as facts.
- Do not interpret missing information as confirmation that something does not exist.
- Avoid repeating the same information across several sections unless the repetition adds a different meaning.
- Do not include detailed requirements, user stories, architecture, implementation plans, or test plans.
- Use version control instead of retaining obsolete approval cycles inside the document.

---

## 1. Document Control

- **Project name:** [Project name]
- **Source request:** `clarified_project_request.md`
- **Prepared by:** [Name]
- **Version:** [Version]
- **Last updated:** [YYYY-MM-DD]
- **Document state:** Draft | Under Clarification | Pending Approval | Closed

## 2. Project Summary

[Summarize the problem, intended user, expected result, first useful software version, and main confirmed limit in one concise paragraph.]

## 3. Background

[Describe the current situation that led to the project.]

## 4. Problem Statement

[State the observable problem without prescribing a technical solution.]

## 5. Why the Project Is Needed

[Explain why the project should be undertaken and why it matters now.]

## 6. Desired Future Situation

[Describe what should be different after the project succeeds.]

## 7. Project Goal

[State one clear result the project should achieve.]

## 8. Expected Outcomes

- [Expected high-level outcome]

## 9. People Involved

### Intended Users

- [Person or group who will use the software]

### Other People Affected

- [Person or group, or `None identified in the approved source`]

### Confirmed Responsibilities

Record only responsibilities confirmed by the source.

- **[Name]:** [Confirmed responsibility]

If no additional responsibility is confirmed, write:

- `No additional responsibilities identified in the approved source.`

## 10. High-Level Scope

### Included

- [High-level scope item]

### Excluded

- [Explicit exclusion]

## 11. MVP Boundary

In this document, the MVP boundary is the smallest useful software scope approved for the first version. It does not include hypotheses, experiments, or business validation.

### Intended User

[Who must be able to use the first version.]

### Minimum Useful Outcome

[What the user must be able to achieve with the first version.]

### Included High-Level Capabilities

- [Capability]

### Explicitly Excluded

- [Excluded capability]

### Confirmed Delivery Limits

- [Confirmed deadline, budget, required environment, or other limit]

### Completion Condition

[An observable condition showing that the approved first-version software scope has been delivered.]

## 12. Constraints

A constraint is a confirmed condition the project must respect and cannot freely change.

- [Confirmed constraint, or `No additional constraints identified in the approved source`]

## 13. Assumptions

An assumption is an unconfirmed statement temporarily treated as true. Do not invent assumptions merely to fill this section.

- [Assumption, or `No assumptions recorded`]

## 14. Dependencies

A dependency is something outside the project that must be available or completed. Do not invent dependencies merely to fill this section.

- [Dependency, or `No dependencies identified in the approved source`]

## 15. Risks and Uncertainties

A risk is an uncertain event that could negatively affect the project. An uncertainty is important missing knowledge.

- **[Risk or uncertainty]:** [Possible impact]

If none are supported by the source, write:

- `No project-level risks or uncertainties identified in the approved source.`

## 16. Success Criteria

Use observable project-level conditions. Do not include implementation details.

- [Observable success condition]

## 17. Confirmed Decisions and Responsibilities

Record only what is confirmed.

- **Person who requested the project:** [Name or `Not identified`]
- **Person who makes project-level decisions:** [Name or `Not assigned in the approved source`]
- **Person who confirms the software meets the agreed scope:** [Name or `Not assigned in the approved source`]
- **Person responsible for building the software:** [Name or `Not assigned in the approved source`]

## Working Questions — Remove Before Approval

Include this temporary section only when missing information prevents a coherent or approvable Project Context.

### Q1 — [Category]

- **Question:** [Plain-language project-level question]
- **Status:** Open | Answered
- **Answered by:** [Person and role or responsibility]
- **Answer:** [Concise answer]
- **Impact:** [What the answer confirms, changes, or excludes]

## 18. Project Context Approval

### Status

- [ ] Ready for User Stories
- [ ] Not Ready

### Reviewed by

- **Name:** [Reviewer name]
- **Role or responsibility:** [How this person is authorized to approve]
- **Date:** [YYYY-MM-DD]

### Blocking Issues or Feedback

[List issues that prevent approval or feedback that must be addressed.]

Write `None` only when `Ready for User Stories` is selected.

### Approval Rule

The document can be closed and passed to user-story definition only when:

- `Ready for User Stories` is selected.
- The reviewer name, responsibility, and date are recorded.
- `Blocking Issues or Feedback` is `None`.

When `Not Ready` is selected, set `Document state` to `Under Clarification`, address the feedback, clear the current approval fields before resubmission, and keep the document open.
