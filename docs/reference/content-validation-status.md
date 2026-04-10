---
content_sources:
  diagrams:
    - id: summary
      type: pie
      source: self-generated
      justification: "Status visualization generated for this guide and grounded in the Microsoft Learn service references listed below."
      based_on:
        - https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
        - https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview
        - https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview
        - https://learn.microsoft.com/en-us/azure/dns/dns-overview
        - https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction
---

# Content Source Validation Status

This page tracks the source validation status of all documentation content, including diagrams and text content. All content must be traceable to official Microsoft Learn documentation.

## Summary

*Generated: 2026-04-10*

| Content Type | Total | MSLearn Adapted | Self-Generated | No Source |
|---|---:|---:|---:|---:|
| Mermaid Diagrams | 81 | 34 | 47 | 0 |
| Text Sections | — | — | — | — |

!!! success "Validation complete"
    All 81 rendered Mermaid diagrams now include `content_sources` frontmatter metadata and `diagram-id` comments.

<!-- diagram-id: summary -->
```mermaid
pie title Content Source Status
    "MSLearn Adapted" : 34
    "Self-Generated" : 47
```

## Validation Categories

### Source Types

| Type | Description | Allowed |
|---|---|---|
| `mslearn` | Content directly from or based on Microsoft Learn | Yes |
| `mslearn-adapted` | Microsoft Learn content adapted for this guide | Yes, with source URL |
| `self-generated` | Original content created for this guide | Requires justification |
| `community` | From community sources | Not for core content |
| `unknown` | Source not documented | Must be validated |

### Diagram Validation Status

- 34 diagrams are marked `mslearn-adapted` and point to primary Microsoft Learn URLs.
- 47 diagrams are marked `self-generated` with justification plus official Learn `based_on` references.
- Every rendered Mermaid block in `docs/` now has a matching `<!-- diagram-id: ... -->` comment.
- Two platform diagrams were redrawn during validation to better align with Microsoft Learn service behavior and placement guidance.

## How to Validate Content

### Step 1: Add Source Metadata to Frontmatter

Add `content_sources` to the document's YAML frontmatter:

```yaml
---
title: How Azure Networking Works
content_sources:
  diagrams:
    - id: architecture-overview
      type: flowchart
      source: mslearn
      mslearn_url: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
      description: "Azure networking architecture"
    - id: request-flow
      type: sequence
      source: self-generated
      justification: "Synthesized from multiple Microsoft Learn articles for clarity"
      based_on:
        - https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
        - https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview
  text:
    - section: "## Summary"
      source: mslearn-adapted
      mslearn_url: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
---
```

### Step 2: Mark Diagram Blocks with IDs

Add an HTML comment before each mermaid block to identify it:

```markdown
```mermaid
flowchart TD
    A[Client] --> B[Azure Networking]
```
```

### Step 3: Run Validation Script

```bash
python3 scripts/validate_content_sources.py
```

### Step 4: Update This Page

```bash
python3 scripts/generate_content_validation_status.py
```

## Validation Rules

!!! danger "Mandatory Rules"
    1. Platform diagrams in `docs/platform/` must have Microsoft Learn sources.
    2. Architecture diagrams must reference official Microsoft documentation.
    3. Troubleshooting flowcharts may be self-generated if they synthesize Microsoft Learn content.
    4. Self-generated content must have a justification field explaining the source basis.

## Official Microsoft Learn References

Use these official sources for diagram validation:

| Topic | Microsoft Learn URL |
|---|---|
| Virtual network overview | https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview |
| Subnets | https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-subnet |
| IP addressing | https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/virtual-network-ip-addresses-overview |
| DNS | https://learn.microsoft.com/en-us/azure/dns/dns-overview |
| Routing | https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview |
| Network security groups | https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview |
| Private endpoints | https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview |
| Hybrid networking | https://learn.microsoft.com/en-us/azure/networking/fundamentals/networking-overview |

## See Also

- [Tutorial Validation Status](validation-status.md)
- [Reference Index](index.md)
