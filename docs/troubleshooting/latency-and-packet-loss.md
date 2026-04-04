# Latency and Packet Loss

Isolating performance bottlenecks in the network path.

| Source | Characteristic | Investigation |
| --- | --- | --- |
| Network RTT | Consistent High Ping. | Check Geography / Hop. |
| App Processing | High Time-to-First-Byte. | Check Backend CPU. |
| Backend Saturation | Spikes during Load. | Check NIC Throttling. |
| ISP / Provider | Random Packet Loss. | Check ExpressRoute MSEE. |

```mermaid
graph TD
    User[Client] -- RTT --> LB[Load Balancer]
    LB -- Processing --> App[App Server]
    App -- Query --> DB[Database]
    LB -- Total --> User
```

!!! note
    Separate network latency (ping/RTT) from application latency (HTTP response time) during triage.

## Sources

- [Test network latency between VMs](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-test-latency)
- [Monitor ExpressRoute performance](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-monitoring-metrics)
