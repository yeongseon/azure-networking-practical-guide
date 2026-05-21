---
content_sources:
  diagrams:
  - id: best-practices-private-endpoint-best-practices-flow
    type: flowchart
    source: mslearn-adapted
    description: Private PaaS access
    based_on:
    - https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview
    - https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns
    - https://learn.microsoft.com/en-us/azure/private-link/manage-private-endpoint
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview
    verified: false
  - claim: Core Azure networking guidance on this page should remain traceable to
      the listed sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview
    verified: false
---

# Private Endpoint Best Practices

Private Endpoint design should cover DNS, subnet policy, public access, approval workflow, and consumer routing.

## Why This Matters

A storage or database service must be reachable privately from selected spokes without breaking public clients unexpectedly.

<!-- diagram-id: best-practices-private-endpoint-best-practices-flow -->
```mermaid
flowchart TD
    A[Classify network path] --> B[Identify owning control]
    B --> C[Apply topic-specific guardrails]
    C --> D[Validate DNS route and security evidence]
    D --> E[Record owner and rollback notes]
```

## Recommended Practices

### 1. Plan DNS before endpoint creation

**Why:** A private endpoint without correct DNS still sends clients to the public endpoint.

**How:** Create or link the correct Private DNS zone and test resolution from consumer VNets.

**Validation:** Client lookup returns the private endpoint IP.

### 2. Control public network access deliberately

**Why:** Turning off public access before consumers resolve private DNS causes outages.

**How:** Sequence private endpoint, DNS validation, firewall rules, and public access changes.

**Validation:** Both private and remaining public clients are tested before enforcement.

### 3. Track approvals and ownership

**Why:** Private endpoint connections can remain pending or orphaned across teams.

**How:** Record service owner, consumer owner, connection status, and delete path.

**Validation:** Connection status and DNS record match the approved consumer.

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

- [Private Endpoint Overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)
- [Private Endpoint Dns](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)
- [Manage Private Endpoint](https://learn.microsoft.com/en-us/azure/private-link/manage-private-endpoint)
