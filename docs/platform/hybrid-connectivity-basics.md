# Hybrid Connectivity Basics

Hybrid connectivity allows you to extend your on-premises network into Azure, enabling seamless communication between local resources and cloud services.

| Feature | VPN Gateway | ExpressRoute |
| --- | --- | --- |
| Bandwidth | Up to 10 Gbps. | 50 Mbps to 10 Gbps |
| Latency | Variable (Internet). | Low/Predictable (Private). |
| Cost | Lower cost. | Higher (Circuit + Port). |
| Best Use Case | Branch offices, Dev/Test. | Critical workloads, Data migrations. |

```mermaid
graph LR
    OnPrem[On-Premises Network] --- VPN[S2S VPN Tunnel]
    VPN --- VNG[Virtual Network Gateway]
    OnPrem --- ER[ExpressRoute Circuit]
    ER --- VNG
    VNG --- VNet[Azure Virtual Network]
```

!!! note
    Hybrid DNS is often the most complex part of a hybrid setup. Consider using Azure DNS Private Resolvers to bridge queries between on-premises and Azure Private DNS Zones.

## Connectivity Planning Matrix

| Constraint | Preferred Option | Planning Focus |
| --- | --- | --- |
| Rapid deployment | VPN Gateway | Shared key, tunnel stability, routing |
| Deterministic latency | ExpressRoute | Circuit provider, redundancy, failover |
| Mixed branch and core workloads | VPN + ExpressRoute | Route preference and segmentation |

## See Also

- [Hybrid Connectivity Best Practices](../best-practices/hybrid-connectivity-best-practices.md)
- [VPN and ExpressRoute Basics](../operations/vpn-and-expressroute-basics.md)
- [Hybrid Connectivity Issues](../troubleshooting/hybrid-connectivity-issues.md)

## Sources

- [About VPN Gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways)
- [ExpressRoute overview](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)
