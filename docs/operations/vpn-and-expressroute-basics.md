# VPN and ExpressRoute Basics

Hybrid connectivity extends on-premises networks to Azure.

| Feature | VPN S2S | ExpressRoute |
| --- | --- | --- |
| Transport | Public Internet (Encrypted) | Private Connection (Layer 2/3) |
| Bandwidth | Up to 10 Gbps | 50 Mbps to 10 Gbps |
| Latency | Higher / Variable | Low / Predictable |
| SLA | 99.9% - 99.95% | 99.9% - 99.95% |

| Readiness Check | VPN | ExpressRoute |
| --- | --- | --- |
| Routing protocol | Optional static or BGP | BGP expected for scale |
| Edge dependency | Internet ISP stability | Provider circuit health |
| Common validation | Tunnel or circuit state is Up | Learned routes are present |

```mermaid
graph LR
    OnPrem[On-Premises] -- ISP/MSEE -- Gate[Azure Gateway]
    Gate -- GatewaySubnet -- VNet[Azure VNet]
    OnPrem -- Encrypted -- Public[VPN Gateway]
```

!!! note
    A gateway subnet size of /27 is recommended to allow for future growth and avoid IP exhaustion.

## See Also

- [Hybrid Connectivity Basics](../platform/hybrid-connectivity-basics.md)
- [Hybrid Connectivity Best Practices](../best-practices/hybrid-connectivity-best-practices.md)
- [Hybrid Connectivity Issues](../troubleshooting/playbooks/routing/hybrid-connectivity-issues.md)

## Sources

- [What is Azure VPN Gateway?](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways)
- [What is Azure ExpressRoute?](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)
