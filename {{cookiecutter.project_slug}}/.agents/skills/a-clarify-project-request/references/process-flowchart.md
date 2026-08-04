# Clarified Project Request Process Flow

Use this flow to explain or verify the process from receiving an informal project request to delivering an approved Clarified Project Request. The flowchart is a visual representation of the workflow defined in `SKILL.md`.

```mermaid
flowchart TD
    A[Receive informal project request] --> B[Preserve the original source]
    B --> C{Does clarified_project_request.md exist?}

    C -->|No| D[Create document from bundled template]
    D --> E[Set Document state to Draft]

    C -->|Yes| F[Load existing document]

    E --> G[Read and analyze the original source]
    F --> G

    G --> H[Draft or update Initial Understanding summary]
    H --> I[Identify critical uncertainties]
    I --> J[Create or update up to 10 project-level critical questions]
    J --> K[Set Document state to Under Clarification]

    K --> L{Are answers available?}

    L -->|No| M[Deliver document for clarification]
    M --> N[Requester or stakeholders provide answers]
    N --> O[Record each answer below its question]

    L -->|Yes| O

    O --> P[Describe the impact of each answer]
    P --> Q[Update Initial Understanding summary]
    Q --> R[Check contradictions, unsupported claims, stale content, and premature technical details]
    R --> S{Do blocking uncertainties remain?}

    S -->|Yes| T[Keep Document state as Under Clarification]
    T --> U[Retain or update open questions]
    U --> V[Request additional clarification]
    V --> N

    S -->|No| W[Set Document state to Pending Approval]
    W --> X[Submit document for human approval]
    X --> Y{Readiness approval}

    Y -->|Not Ready| Z[Record approver and blocking issues]
    Z --> AA[Set Document state to Closed]

    Y -->|Ready| AB[Record approver name, role, date, and Blocking Issues as None]
    AB --> AC[Set Document state to Closed]
    AC --> AD[Deliver approved Clarified Project Request]
    AD --> AE[Pass document to Project Context Formation skill]
```
