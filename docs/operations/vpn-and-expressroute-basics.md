# VPN and ExpressRoute Basics

Hybrid connectivity extends on-premises networks to Azure.

| Feature | VPN S2S | ExpressRoute |
| --- | --- | --- |
| Transport | Public Internet (Encrypted) | Private Connection (Layer 2/3) |
| Bandwidth | Up to 10 Gbps | Up to 100 Gbps |
| Latency | Higher / Variable | Low / Predictable |
| SLA | 99.9% - 99.95% | 99.9% - 99.95% |

```mermaid
graph LR
    OnPrem[On-Premises] -- ISP/MSEE -- Gate[Azure Gateway]
    Gate -- GatewaySubnet -- VNet[Azure VNet]
    OnPrem -- Encrypted -- Public[VPN Gateway]
```

!!! note
    A gateway subnet size of /27 is recommended to allow for future growth and avoid IP exhaustion.

## Sources

- [What is Azure VPN Gateway?](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways)
- [What is Azure ExpressRoute?](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)
