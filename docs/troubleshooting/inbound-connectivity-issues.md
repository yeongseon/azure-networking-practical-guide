# Inbound Connectivity Issues

Resolving access failures for services exposed to the internet or VNet.

| Cause | Indicator | Resolution |
| --- | --- | --- |
| Health Probe Fail | Backends show Unhealthy. | Check Backend Service/Port. |
| NSG Inbound Deny | Traffic dropped at NIC. | Add Inbound Allow Rule. |
| Firewall Rule | Firewall drops packet. | Add DNAT / Application Rule. |
| Frontend IP | Resource unreachable. | Verify Public IP assignment. |

```mermaid
graph TD
    Client[Request] --> Front[Frontend IP]
    Front --> Firewall[Firewall Rules]
    Firewall --> LB[Load Balancer]
    LB --> Probe[Health Probe OK?]
    Probe -- No --> Back[Check Backend Service]
    Probe -- Yes --> NSG[Inbound NSG Check]
```

!!! tip
    Verify health probe status in the Load Balancer or Application Gateway metrics before checking OS firewall.

## Sources

- [Troubleshoot Application Gateway connectivity](https://learn.microsoft.com/en-us/azure/application-gateway/troubleshoot-app-service-redirection-app-service-url)
- [Troubleshoot Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)
