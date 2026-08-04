# Workflow

The workflow has two explicit entry branches. Both branches join only after the requirement and repository handling have been established.

## Written workflow

1. Load the available inputs.
2. Determine whether the mode is `initial release` or `product increment`.

### Initial release branch

3. Verify that `sdlc_docs/00_inception/project_context.md` is approved.
4. Extract the requirements for the first release.
5. Create the initial `product_requirements.md` structure.
6. Set all repository issue references to `Not created`.
7. Continue to the common refinement workflow at step 14.

### Product increment branch

8. Load the current `product_requirements.md` and only the imported repository issues that passed triage.
9. Process each imported issue as a new unapproved requirement; do not rewrite approved requirements.
10. Determine whether the original issue is a `broad-request` or an existing `user-story`.
11. For a `broad-request`, keep the original issue as the requirement source and future repository container; generate missing user stories later as new sub-issues.
12. For an existing `user-story`, create a documentation-only requirement, reuse the original issue for the story, and do not create a requirement issue or duplicate story issue.
13. Continue to the common refinement workflow at step 14.

### Common refinement and approval workflow

14. Determine whether blocking information is missing.
15. If information is missing, interview the user and update only the affected unapproved requirement or draft story.
16. Generate one or more user stories for a requirement, or refine the existing story when the source issue already represents one.
17. Add testable acceptance criteria to every story.
18. Present the requirement, stories, criteria, source issue, and intended repository action for review.
19. Determine whether the user approves the requirement and its stories.
20. If not approved, set the affected content to `Under Clarification` and repeat from step 14.
21. If approved, mark the requirement and reviewed stories `Approved`.
22. Update the overview table, issue references, approver, and approval date.
23. Save `sdlc_docs/01_requirements/product_requirements.md`.

## Flowchart

```mermaid
flowchart TD
    A[Load available inputs] --> B{Initial release or product increment?}

    B -- Initial release --> C[Verify approved project_context.md]
    C --> D[Extract requirements for the first release]
    D --> E[Create initial product_requirements.md structure]
    E --> F[Set repository issue references to Not created]

    B -- Product increment --> G[Load current product_requirements.md and triaged imported issues]
    G --> H[Add each imported issue as a new unapproved requirement]
    H --> I{Broad request or existing user story?}
    I -- Broad request --> J[Keep original issue as source and future requirement container]
    I -- Existing user story --> K[Create documentation-only requirement and reuse original issue for the story]

    F --> L{Is blocking information missing?}
    J --> L
    K --> L

    L -- Yes --> M[Interview user and update affected unapproved content]
    M --> N[Generate stories or refine the existing story]
    L -- No --> N
    N --> O[Add testable acceptance criteria]
    O --> P[Present requirement, stories, criteria, source issue, and repository action]
    P --> Q{Does the user approve?}
    Q -- No --> R[Set affected content to Under Clarification]
    R --> L
    Q -- Yes --> S[Mark requirement and reviewed stories Approved]
    S --> T[Update overview, issue references, approver, and approval date]
    T --> U[Save product_requirements.md]
```

## Branch outcomes

### Initial release

The document produces approved requirements and stories first. Repository references remain `Not created` until the synchronization skill creates the corresponding issues.

### Product increment from a broad request

The original broad issue remains the requirement source and may later serve as the parent container. Newly generated stories are returned to the repository as new sub-issues.

### Product increment from an existing user story

The original issue remains the only repository issue for that story. The requirement exists only in the documentation, and the synchronization skill refines the original issue instead of creating a parent or duplicate issue.
