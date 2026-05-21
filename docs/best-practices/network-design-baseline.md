---
content_sources:
  diagrams:
  - id: best-practices-network-design-baseline-flow
    type: flowchart
    source: mslearn-adapted
    description: Baseline control set
    based_on:
    - https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm
    - https://learn.microsoft.com/en-us/azure/architecture/networking/guide/network-level-segmentation
    - https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm
    verified: false
  - claim: Core Azure networking guidance on this page should remain traceable to
      the listed sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm
    verified: false
---

# Network Design Baseline

A network baseline documents address space, segmentation, routing, DNS, security, and connectivity ownership.

## Why This Matters

A new landing zone needs consistent network standards before application teams create subnets and private endpoints.

<!-- diagram-id: best-practices-network-design-baseline-flow -->
```mermaid
flowchart TD
    A[Classify network path] --> B[Identify owning control]
    B --> C[Apply topic-specific guardrails]
    C --> D[Validate DNS route and security evidence]
    D --> E[Record owner and rollback notes]
```

## Recommended Practices

### 1. Plan non-overlapping address space

**Why:** Overlapping CIDR ranges break peering, routing, VPN, and ExpressRoute growth.

**How:** Reserve ranges for hub, spokes, gateways, firewall, private endpoints, and future regions.

**Validation:** Address plan shows no overlap with connected networks.

### 2. Assign ownership by subnet and path

**Why:** Ambiguous subnet ownership causes stalled changes and unsafe NSG edits.

**How:** Record owner, purpose, route table, NSG, DNS zone, and allowed dependencies for each subnet.

**Validation:** Subnet inventory has owner and control attachments.

### 3. Create an evidence standard

**Why:** Networking incidents need route, DNS, and security evidence, not only resource lists.

**How:** Require effective routes, effective security rules, DNS lookup, and connection tests for changes.

**Validation:** Change records include the evidence pack before and after the change.

### CLI review example

```bash
az network vnet show \
    --resource-group $RG \
    --name $VNET_NAME \
    --query "{name:name,addressSpace:addressSpace.addressPrefixes,subnets:subnets[].name}" \
    --output json

az network nic show-effective-route-table \
    --resource-group $RG \
    --name $NIC_NAME \
    --output table

az network nic list-effective-nsg \
    --resource-group $RG \
    --name $NIC_NAME \
    --output table
```

| Element | Purpose |
|---|---|
| `$RG` | Resource group containing the networking resources. |
| `$VNET_NAME` | Virtual network being created, linked, or inspected. |
| `$NIC_NAME` | Network interface used for effective rule or route checks. |
| `--resource-group` | Scopes the command to the intended resource group. |
| `--name` | Identifies the target Azure networking resource. |
| `--query` | Filters output to the evidence operators need. |
| `--output` | Controls output format for review or automation. |
| Expected result | Command succeeds and returns resource state, path evidence, or operation status for the change record. |

## Common Mistakes / Anti-Patterns

- Reviewing a single resource without validating DNS, route, and security behavior from the actual source subnet.
- Making broad allow or default-route changes without recording the owner and rollback path.
- Disabling public access or changing peering and route propagation before private path validation.

## Validation Checklist

- [ ] Source, destination, protocol, port, DNS name, and owner are recorded.
- [ ] Effective route and effective security rule evidence matches the intended path.
- [ ] DNS resolution is tested from the consumer network when private connectivity is involved.
- [ ] Rollback command or manual rollback path is documented.

## See Also

- [Network Design Baseline](network-design-baseline.md)
- [Operations](../operations/index.md)
- [Troubleshooting](../troubleshooting/index.md)

## Sources

- [Virtual Network Vnet Plan Design Arm](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm)
- [Network Level Segmentation](https://learn.microsoft.com/en-us/azure/architecture/networking/guide/network-level-segmentation)
- [Virtual Networks Overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
