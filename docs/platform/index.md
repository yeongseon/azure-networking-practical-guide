---
content_sources:
  diagrams:
  - id: index
    type: flowchart
    source: self-generated
    justification: Guide navigation diagram created for this repository and grounded
      in Microsoft Learn networking overview content.
    based_on:
    - https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
    - https://learn.microsoft.com/en-us/azure/networking/fundamentals/networking-overview
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
    verified: false
  - claim: Core Azure networking guidance on this page should remain traceable to
      the listed sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
    verified: false
---

# Platform Fundamentals

This section provides a deep dive into the core components of Azure networking. Understanding these fundamentals is necessary for designing secure, scalable, and resilient cloud architectures.

| Topic | Description |
| --- | --- |
| [How Azure Networking Works](how-azure-networking-works.md) | High-level overview of region, VNet, and packet paths. |
| [VNet and Subnet Basics](vnet-and-subnet-basics.md) | Core building blocks for network isolation and IP design. |
| [IP Addressing](ip-addressing.md) | Management of public and private IP resources. |
| [DNS Basics](dns-basics.md) | Resolution mechanisms for cloud and hybrid environments. |
| [Routing Basics](routing-basics.md) | Traffic steering using system and user-defined routes. |
| [Network Security Basics](network-security-basics.md) | Protective layers including NSGs and Firewalls. |
| [Load Balancing Options](load-balancing-options.md) | Distributing traffic across compute resources. |
| [Private Connectivity Options](private-connectivity-options.md) | Secure access to Azure PaaS via Private Link. |
| [Hybrid Connectivity Basics](hybrid-connectivity-basics.md) | Connecting on-premises sites to Azure VNets. |

<!-- diagram-id: index -->
```mermaid
graph TD
    A[VNet & Subnets] --> B[IP Addressing]
    A --> C[Routing]
    A --> D[Security]
    B --> E[DNS]
    C --> F[Hybrid Connectivity]
    D --> G[Load Balancing]
    E --> H[Private Connectivity]
```

!!! tip
    Start with VNet and subnet design first, then validate routing, security, and DNS in that order before selecting connectivity patterns.

## See Also

- [Start Here Overview](../start-here/overview.md)
- [How Azure Networking Works](how-azure-networking-works.md)
- [VNet and Subnet Basics](vnet-and-subnet-basics.md)

## Sources

- [Azure Virtual Network concepts](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
- [Azure networking services overview](https://learn.microsoft.com/en-us/azure/networking/fundamentals/networking-overview)
