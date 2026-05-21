---
content_sources:
  diagrams:
  - id: best-practices-routing-best-practices-flow
    type: flowchart
    source: mslearn-adapted
    description: Route intent
    based_on:
    - https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview
    - https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview
    - https://learn.microsoft.com/en-us/azure/firewall/overview
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview
    verified: false
  - claim: Core Azure networking guidance on this page should remain traceable to
      the listed sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview
    verified: false
---

# Routing Best Practices

Routing guidance should make next hops, asymmetric paths, peering transit, and appliance insertion explicit.

## Why This Matters

A hub-and-spoke workload sends internet-bound traffic through Azure Firewall while keeping private east-west traffic predictable.

<!-- diagram-id: best-practices-routing-best-practices-flow -->
```mermaid
flowchart TD
    A[Classify network path] --> B[Identify owning control]
    B --> C[Apply topic-specific guardrails]
    C --> D[Validate DNS route and security evidence]
    D --> E[Record owner and rollback notes]
```

## Recommended Practices

### 1. Document route ownership

**Why:** UDRs, BGP, system routes, and peering settings can override each other.

**How:** Record which team owns each route table and why each prefix has a next hop.

**Validation:** Effective route output matches the intended next hop.

### 2. Avoid accidental asymmetry

**Why:** Return traffic through a different firewall or gateway can break stateful inspection.

**How:** Validate both source-to-destination and return paths before cutover.

**Validation:** Connection tests and effective routes prove symmetric behavior where required.

### 3. Treat peering transit as a design decision

**Why:** Peering does not automatically create transitive routing.

**How:** Use hub appliances or gateways intentionally and configure forwarded traffic only where needed.

**Validation:** Peering flags and route tables match the transit design.

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

- [Virtual Networks Udr Overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)
- [Virtual Network Peering Overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview)
- [Overview](https://learn.microsoft.com/en-us/azure/firewall/overview)
