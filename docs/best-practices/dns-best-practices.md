---
content_sources:
  diagrams:
  - id: best-practices-dns-best-practices-flow
    type: flowchart
    source: mslearn-adapted
    description: Name resolution
    based_on:
    - https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone
    - https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns
    - https://learn.microsoft.com/en-us/azure/dns/dns-overview
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone
    verified: false
  - claim: Core Azure networking guidance on this page should remain traceable to
      the listed sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone
    verified: false
---

# DNS Best Practices

DNS design must define resolver ownership, private zone links, split-horizon records, and failure evidence.

## Why This Matters

A Private Endpoint deployment fails because clients resolve the public endpoint instead of the private IP.

<!-- diagram-id: best-practices-dns-best-practices-flow -->
```mermaid
flowchart TD
    A[Classify network path] --> B[Identify owning control]
    B --> C[Apply topic-specific guardrails]
    C --> D[Validate DNS route and security evidence]
    D --> E[Record owner and rollback notes]
```

## Recommended Practices

### 1. Make resolution path explicit

**Why:** Private connectivity often fails because clients use the wrong resolver or zone link.

**How:** Document resolver IPs, forwarding rules, private zones, and VNet links.

**Validation:** Queries from each client subnet resolve to the intended address.

### 2. Separate public and private records intentionally

**Why:** Split-horizon records can hide whether traffic uses private or public endpoints.

**How:** Keep private zones linked only to networks that should resolve private addresses.

**Validation:** DNS tests include client subnet, resolver, record type, and returned IP.

### 3. Monitor stale and conflicting records

**Why:** Old A records can route clients to deleted private endpoints or wrong appliances.

**How:** Review zone records during endpoint lifecycle changes.

**Validation:** Record inventory matches live private endpoint NICs.

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

- [Private Dns Privatednszone](https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone)
- [Private Endpoint Dns](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)
- [Dns Overview](https://learn.microsoft.com/en-us/azure/dns/dns-overview)
