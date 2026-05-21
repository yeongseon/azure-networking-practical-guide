---
content_sources:
  diagrams:
  - id: best-practices-nsg-and-firewall-best-practices-flow
    type: flowchart
    source: mslearn-adapted
    description: Layered controls
    based_on:
    - https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview
    - https://learn.microsoft.com/en-us/azure/firewall/overview
    - https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-ip-flow-verify-overview
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview
    verified: false
  - claim: Core Azure networking guidance on this page should remain traceable to
      the listed sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview
    verified: false
---

# NSG and Firewall Best Practices

NSGs and Azure Firewall should provide layered controls with clear rule intent and observable enforcement.

## Why This Matters

A production subnet needs local allow rules, firewall egress control, and evidence that management ports are not broadly exposed.

<!-- diagram-id: best-practices-nsg-and-firewall-best-practices-flow -->
```mermaid
flowchart TD
    A[Classify network path] --> B[Identify owning control]
    B --> C[Apply topic-specific guardrails]
    C --> D[Validate DNS route and security evidence]
    D --> E[Record owner and rollback notes]
```

## Recommended Practices

### 1. Use NSGs for subnet and NIC intent

**Why:** NSGs are fast local controls but can become unreadable when rules are broad or duplicated.

**How:** Name rules by application intent and keep priorities grouped by source and destination.

**Validation:** Effective security rules show only intended flows.

### 2. Use Firewall for centralized inspection

**Why:** Firewall policy is better for shared egress, FQDN control, threat intelligence, and forced tunneling.

**How:** Route traffic to the firewall only where inspection is required and avoid hairpinning unrelated flows.

**Validation:** Firewall logs and UDRs prove the inspected path.

### 3. Review deny behavior before rollout

**Why:** A deny rule can block health probes, DNS, identity, or update traffic.

**How:** Test required dependencies before enforcing broad denies.

**Validation:** Packet path tests show allowed dependencies still work.

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

- [Network Security Groups Overview](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)
- [Overview](https://learn.microsoft.com/en-us/azure/firewall/overview)
- [Network Watcher Ip Flow Verify Overview](https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-ip-flow-verify-overview)
