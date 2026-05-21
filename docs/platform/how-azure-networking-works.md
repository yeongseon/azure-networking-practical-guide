---
content_sources:
  diagrams:
  - id: how-azure-networking-works
    type: flowchart
    source: mslearn-adapted
    mslearn_url: https://learn.microsoft.com/en-us/azure/security/fundamentals/network-best-practices
    based_on:
    - https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/network-topology-and-connectivity
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/security/fundamentals/network-best-practices
    verified: false
  - claim: Core Azure networking guidance on this page should remain traceable to
      the listed sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/security/fundamentals/network-best-practices
    verified: false
---

# How Azure Networking Works

Azure Networking provides the infrastructure to connect cloud services and on-premises environments. It's built on a global fiber-optic network that uses Software Defined Networking (SDN) to manage traffic flows.

| Component | Responsibility | Managed By |
| --- | --- | --- |
| Physical Network | Fiber, routers, switches | Microsoft |
| VNet | Address space, logical isolation | User |
| Subnet | Micro-segmentation | User |
| Network Interface (NIC) | Virtual hardware connection | User |
| NSG Rules | Access control lists | User |
| Route Table | Custom traffic steering | User |

<!-- diagram-id: how-azure-networking-works -->
```mermaid
graph TD
    VNet[Azure Virtual Network] --> Subnet[Subnet]
    Subnet --> VM[Virtual Machine]
    VM --> NIC[Network Interface]
    Subnet -. association .-> NSG[Network Security Group]
    Subnet -. association .-> RT[Route Table]
    RT --> Dest{Traffic destination}
    Dest --> Internet[Internet]
    Dest --> Peering[Peered VNet]
    Dest --> Hybrid[VPN or ExpressRoute]
```

!!! note
    Azure uses a massive global backbone network. Traffic between Azure regions stays on this backbone and does not traverse the public internet unless explicitly configured.

## See Also

- [VNet and Subnet Basics](vnet-and-subnet-basics.md)
- [Routing Basics](routing-basics.md)
- [Network Security Basics](network-security-basics.md)

## Sources

- [Azure network security fundamentals](https://learn.microsoft.com/en-us/azure/security/fundamentals/network-best-practices)
- [VNet architecture and design](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/network-topology-and-connectivity)
