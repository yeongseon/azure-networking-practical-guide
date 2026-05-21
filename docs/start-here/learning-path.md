---
content_sources:
  diagrams:
  - id: progression-flow
    type: flowchart
    source: self-generated
    justification: Synthesized quick-reference diagram for this guide from Microsoft
      Learn networking documentation.
    based_on:
    - https://learn.microsoft.com/en-us/training/modules/azure-networking-fundamentals/
    - https://learn.microsoft.com/en-us/training/browse/?products=azure-networking
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/training/modules/azure-networking-fundamentals/
    verified: false
  - claim: Core Azure networking guidance on this page should remain traceable to
      the listed sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/training/modules/azure-networking-fundamentals/
    verified: false
---

# Learning Path

Follow a tailored journey based on your professional role and needs.

## Path Recommendations

| Path | Audience | Page Sequence |
|------|----------|---------------|
| Beginner | Cloud Novice | Overview → Platform → Operations |
| Operator | SRE / SysAdmin | Platform → Operations → Best Practices |
| Troubleshooter | Support / Dev | Net vs Conn → Troubleshooting → Reference |
| PE/DNS Focus | App Architect | Overview → Private Endpoints → Reference |

## Progression Flow

<!-- diagram-id: progression-flow -->
```mermaid
graph TD
    B[Beginner] --> F[Foundations]
    O[Operator] --> S[Scaling & Sec]
    T[Troubleshooter] --> D[Diagnostics]
    P[PE/DNS Expert] --> A[Architecture]
```

!!! tip
    If you're in an urgent "outage" situation, skip the learning paths and head directly to [Troubleshooting](../troubleshooting/index.md).

## See Also

- [Overview](overview.md)
- [Platform Fundamentals](../platform/index.md)
- [Best Practices](../best-practices/index.md)

## Sources
- [Azure Networking Fundamentals](https://learn.microsoft.com/en-us/training/modules/azure-networking-fundamentals/)
- [Microsoft Learn Training Path](https://learn.microsoft.com/en-us/training/browse/?products=azure-networking)
