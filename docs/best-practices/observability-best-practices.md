---
content_sources:
  diagrams:
  - id: best-practices-observability-best-practices-flow
    type: flowchart
    source: mslearn-adapted
    description: Network evidence
    based_on:
    - https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-monitoring-overview
    - https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-ip-flow-verify-overview
    - https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-monitoring-overview
    verified: false
  - claim: Core Azure networking guidance on this page should remain traceable to
      the listed sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-monitoring-overview
    verified: false
---

# Observability Best Practices

Network observability should collect path, rule, DNS, flow, and packet evidence before an outage forces guesswork.

## Why This Matters

A service team needs to prove whether packet loss comes from NSG, routing, DNS, load balancer, or the application.

<!-- diagram-id: best-practices-observability-best-practices-flow -->
```mermaid
flowchart TD
    A[Classify network path] --> B[Identify owning control]
    B --> C[Apply topic-specific guardrails]
    C --> D[Validate DNS route and security evidence]
    D --> E[Record owner and rollback notes]
```

## Recommended Practices

### 1. Capture the packet path

**Why:** Resource health alone does not explain route or security decisions.

**How:** Use Network Watcher tools such as IP flow verify, next hop, connection troubleshoot, and packet capture.

**Validation:** Evidence identifies the evaluated rule or next hop.

### 2. Correlate logs with topology

**Why:** Flow logs and firewall logs are hard to interpret without subnet and route context.

**How:** Keep topology diagrams, route tables, NSGs, and DNS zones linked from incident records.

**Validation:** Triage notes connect telemetry to the expected path.

### 3. Alert on broken dependencies

**Why:** Connectivity can fail through DNS, gateway, firewall, load balancer, or private endpoint status.

**How:** Use service-level and network-level alerts together.

**Validation:** Alerts identify owner, path, and runbook.

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

- [Network Watcher Monitoring Overview](https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-monitoring-overview)
- [Network Watcher Ip Flow Verify Overview](https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-ip-flow-verify-overview)
- [Connection Monitor Overview](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)
