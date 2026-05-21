---
content_sources:
  diagrams:
  - id: best-practices-cost-awareness-best-practices-flow
    type: flowchart
    source: mslearn-adapted
    description: Network cost control
    based_on:
    - https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-best-practices
    - https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses
    - https://learn.microsoft.com/en-us/azure/nat-gateway/nat-overview
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-best-practices
    verified: false
  - claim: Core Azure networking guidance on this page should remain traceable to
      the listed sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-best-practices
    verified: false
---

# Cost Awareness Best Practices

Networking cost review should preserve availability and inspection requirements while avoiding idle or overbuilt resources.

## Why This Matters

A subscription contains unused public IPs, old gateways, over-provisioned firewalls, and private endpoint sprawl.

<!-- diagram-id: best-practices-cost-awareness-best-practices-flow -->
```mermaid
flowchart TD
    A[Classify network path] --> B[Identify owning control]
    B --> C[Apply topic-specific guardrails]
    C --> D[Validate DNS route and security evidence]
    D --> E[Record owner and rollback notes]
```

## Recommended Practices

### 1. Classify shared services

**Why:** Gateways, firewalls, Bastion, and NAT gateways often outlive the workload that requested them.

**How:** Tag shared networking resources with owner, purpose, environment, and review date.

**Validation:** Monthly inventory has owner decisions for retained resources.

### 2. Right-size gateways and inspection tiers

**Why:** Under-sizing breaks throughput; over-sizing wastes budget.

**How:** Compare observed throughput, connection count, and availability needs before SKU changes.

**Validation:** Metrics justify the selected gateway or firewall SKU.

### 3. Review endpoint sprawl

**Why:** Private endpoints, public IPs, DNS zones, and load balancers can accumulate quietly.

**How:** Inventory detached, idle, or duplicated connectivity resources.

**Validation:** Cleanup report lists deleted or justified retained resources.

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

- [Cost Mgt Best Practices](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-best-practices)
- [Public Ip Addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)
- [Nat Overview](https://learn.microsoft.com/en-us/azure/nat-gateway/nat-overview)
