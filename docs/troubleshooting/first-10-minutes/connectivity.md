---
content_sources:
  diagrams:
    - id: quick-context
      type: flowchart
      source: self-generated
      justification: Synthesized troubleshooting flow for this guide from Microsoft Learn diagnostic and service documentation.
      based_on:
        - https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview
        - https://learn.microsoft.com/en-us/azure/network-watcher/diagnose-vm-network-routing-problem
content_validation:
  status: verified
  last_reviewed: '2026-07-25'
  reviewer: agent
  core_claims:
    - claim: Connection Troubleshoot can quickly test end-to-end connectivity between Azure resources and destinations.
      source: https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview
      verified: true
    - claim: Azure routing diagnostics help determine whether effective routes are causing connectivity problems.
      source: https://learn.microsoft.com/en-us/azure/network-watcher/diagnose-vm-network-routing-problem
      verified: true
---
# First 10 Minutes: Connectivity

## Quick Context
Use this checklist when the symptom is reachability, packet loss, intermittent failure, or latency. The first goal is to separate DNS, path, policy, and target health.

<!-- diagram-id: quick-context -->
```mermaid
flowchart TD
    A[Reachability symptom] --> B{Name resolves correctly?}
    B -->|No| C[Switch to DNS checklist]
    B -->|Yes| D{Next hop expected?}
    D -->|No| E[Switch to Routing checklist]
    D -->|Yes| F{Policy allows flow?}
    F -->|No| G[Open policy/routing playbook]
    F -->|Yes| H[Check listener, probes, or latency]
```

## Step 1: Prove whether this is name-based or IP-based
- Run an IP-only test and a name-based test.
- Good signal: both fail the same way, meaning DNS is less likely.
- Bad signal: IP works but FQDN fails, meaning DNS is likely primary.

## Step 2: Check the expected path
- Use effective routes or next-hop diagnostics.
- Good signal: traffic takes the intended peering, gateway, or internet path.
- Bad signal: traffic exits to an unexpected NVA, gateway, or public path.

## Step 3: Check allow/deny outcome
- Use effective NSG, IP Flow Verify, and firewall/NVA logs.
- Good signal: an allow path clearly matches source, destination, and port.
- Bad signal: implicit or explicit deny matches first.

## Step 4: Confirm listener or probe health
- For inbound issues, validate frontend IP, backend health, and probe status.
- For outbound issues, validate dependency listener and port reachability.
- Good signal: TCP handshake reaches the correct listener.
- Bad signal: probe unhealthy, port closed, or connection reset/refused.

## Step 5: If the issue is time-based, switch to timeline mode
- Compare failures against load, route changes, DNS TTL expiry, or tunnel events.
- Good signal: stable baseline with no time-based spikes.
- Bad signal: repeated burst windows or periodic flapping.

## Decision points
- **Inbound path issue** -> [Inbound Connectivity Issues](../playbooks/connectivity/inbound-connectivity-issues.md)
- **Outbound path issue** -> [Outbound Connectivity Issues](../playbooks/connectivity/outbound-connectivity-issues.md)
- **Private Endpoint issue** -> [Cannot Reach Private Endpoint](../playbooks/connectivity/cannot-reach-private-endpoint.md)
- **Intermittent issue** -> [Intermittent Network Failures](../playbooks/connectivity/intermittent-network-failures.md)
- **Latency or loss** -> [Latency and Packet Loss](../playbooks/connectivity/latency-and-packet-loss.md)

```bash
az network watcher test-connectivity --source-resource <source-id> --dest-address <fqdn-or-ip> --dest-port 443
az network nic show-effective-route-table --resource-group <resource-group> --name <nic-name>
az network nic list-effective-nsg --resource-group <resource-group> --name <nic-name>
```

| Command | Purpose |
| --- | --- |
| `az network watcher test-connectivity` | Test reachability between a source resource and a destination. |
| `--source-resource` | Resource ID of the source to test from. |
| `--dest-address` | Destination FQDN or IP address. |
| `--dest-port` | Destination TCP port to test. |
| `az network nic show-effective-route-table` | Show the effective routes applied to a network interface. |
| `az network nic list-effective-nsg` | List the effective NSG rules applied to a network interface. |
| `--resource-group` | Resource group that contains the network interface. |
| `--name` | Name of the network interface to inspect. |

## See Also

- [DNS Checklist](dns.md)
- [Routing Checklist](routing.md)
- [Evidence Map](../evidence-map.md)
- [Playbooks Index](../playbooks/index.md)

## Sources

- [Connection troubleshoot in Azure Network Watcher](https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview)
- [Diagnose VM network routing problems](https://learn.microsoft.com/en-us/azure/network-watcher/diagnose-vm-network-routing-problem)
