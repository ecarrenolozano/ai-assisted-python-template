# Clarified Project Request Template

# Clarified Project Request

## How to Use This Document

This document transforms an informal project request into a concise, clarified, and formally approved input for Project Context formation.

Follow these steps in order:

1. Complete the source information in Section 1.
2. Read the original request completely without modifying it.
3. Use the guiding questions in Section 2 to write the initial summary.
4. Use only information supported by the source or confirmed clarifications.
5. Use cautious language when information has not been confirmed.
6. Identify only uncertainties that could materially change the Project Context.
7. Record no more than 10 project-level questions in Section 3.
8. Send each question to the person with the knowledge or authority to answer it.
9. Record each answer directly below its corresponding question.
10. Use the `Impact` field to state what the answer confirms, changes, or excludes.
11. After receiving answers, return to Section 2 and update the summary.
12. Remove uncertainty language for information that has been confirmed.
13. Keep unresolved uncertainties visible.
14. Remove unused question blocks and placeholders.
15. Do not include detailed requirements, user stories, architecture, implementation decisions, or test plans.
16. Set `Document state` to `Pending Approval` only when no blocking uncertainties remain.
17. Submit the completed document to the designated approver.
18. Set `Document state` to `Closed` only after the approver selects `Ready` or `Not Ready`.
19. Pass the document to Project Context formation only when Section 4 is marked `Ready` and `Blocking Issues` is `None`.

### Editing Rules

- Preserve the original request as an independent source file.
- Keep the document concise.
- Prefer short paragraphs and direct statements.
- Distinguish confirmed information from interpretation.
- Do not present assumptions as facts.
- Treat mentioned technologies as proposed solutions unless they are confirmed constraints.
- Keep critical questions at the project level.
- Defer detailed functional and technical questions to later stages.
- Do not add questions merely to reach the maximum of 10.
- Use version-control history instead of retaining obsolete summaries in the document.

### Final Review

Before requesting approval:

1. Update the summary with all confirmed clarifications.
2. Verify that every answered question includes its impact.
3. Keep unresolved questions marked as `Open`.
4. Remove unused placeholders and empty question blocks.
5. Confirm that the document contains no detailed requirements, architecture, or implementation decisions.
6. Record unresolved blocking issues in Section 4.
7. Set `Document state` to `Pending Approval`.
8. Submit the document to the designated approver.

---

## 1. Source

- **Original document:** `[source path or reference]`
- **Requester:** [Person or group that submitted the request]
- **Date received:** [YYYY-MM-DD]
- **Source type:** [Document | Email | Meeting notes | Personal idea | Other]
- **Prepared by:** [Name]
- **Document state:** Draft | Under Clarification | Pending Approval | Closed

## 2. Initial Understanding

### Guiding Questions

- What appears to be happening currently?
- Who appears to be affected?
- What does the requester appear to want to change?
- What general outcome appears to be expected?
- Does the request mention any important deadline, constraint, or proposed solution?
- What important information remains unclear?

### Summary Template

> Currently, **[person, group, or organization]** experiences **[problem or current situation]**. The requester appears to want **[general change or project intention]** so that **[expected benefit or outcome]**. The request mentions **[important constraints, deadlines, or proposed solutions]**. However, **[main uncertainties requiring clarification]** are not yet clear.

### Summary

[Replace this text with the current summary. Update it after every meaningful clarification round.]

## 3. Critical Questions

Create only the questions needed to clarify information that could materially change the Project Context. Use a maximum of 10 questions.

Questions may address the problem or opportunity, expected outcome, users or beneficiaries, rationale, initial project boundary, constraints or deadlines, project-level success, ownership or approval, material dependencies, material risks, or other unresolved project-level information.

Do not use this section to define detailed requirements or technical design.

### Q1 — [Project-level category]

- **Question:** [Question]
- **Status:** Open | Answered
- **Answered by:** [Person and role]
- **Answer:** [Concise answer]
- **Impact:** [What the answer confirms, changes, or excludes]

[Repeat the block only as needed, up to Q10. Remove unused blocks.]

## 4. Readiness Approval

### Status

- [ ] Ready
- [ ] Not Ready

### Approved by

- **Name:** [Approver name]
- **Role:** [Approver role]
- **Date:** [YYYY-MM-DD]

### Blocking Issues

[List unresolved issues that prevent approval.]

Write `None` when the document is approved.

### Approval Rule

The document can be passed to the Project Context Formation skill only when:

- `Ready` is selected.
- The approver's name, role, and approval date are recorded.
- `Blocking Issues` is `None`.
