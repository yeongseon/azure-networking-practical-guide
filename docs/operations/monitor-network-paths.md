# Monitor Network Paths

Visibility into traffic flow and path performance.

| Tool | Capability | Data Type |
| --- | --- | --- |
| Connection Monitor | End-to-end path testing. | RTT, Loss, Hop. |
| VNet Flow Logs | Detailed traffic auditing. | Rule Match, Tuple. |
| Traffic Analytics | Visualizing flow patterns. | Geo-map, Security. |
| Network Watcher | Resource diagnostic tools. | IP Flow, Next Hop. |

| Monitoring Signal | Threshold Example | Action |
| --- | --- | --- |
| Latency increase | RTT > baseline + 30% | Compare hop-level path changes. |
| Packet loss | Loss > 1% sustained | Inspect provider path and NSG drops. |
| Flow anomaly | Unexpected deny spikes | Review recent policy updates. |

```mermaid
graph TD
    Agent[Agent/VM] -- Test --> Target[Resource/URL]
    Target -- Data --> Log[Log Analytics]
    Log -- Analysis --> Visual[Dashboard/Alerts]
```

!!! tip
    Establish baseline metrics for latency and packet loss before making significant network changes.

## See Also

- [Observability Best Practices](../best-practices/observability-best-practices.md)
- [Packet Capture and Diagnostics](./packet-capture-and-diagnostics.md)
- [Latency and Packet Loss](../troubleshooting/playbooks/connectivity/latency-and-packet-loss.md)

## Sources

- [What is Azure Network Watcher?](https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-overview)
- [Monitor networks with Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)
