# Hybrid Connectivity Issues

Resolving tunnel and routing failures across VPN or ExpressRoute.

| Cause | Indicator | Resolution |
| --- | --- | --- |
| BGP State: Down | Routes not appearing in Azure. | Check BGP Peering IP / ASN. |
| Missing Routes | On-prem CIDR not advertised. | Update Local Network Gateway. |
| Tunnel State: Down | VPN Phase 1/2 mismatch. | Align IKE/IPSec Policy. |
| MTU Issues | Fragmentation drops. | Clamp MSS or lower MTU. |

| Validation Point | View | Success Criteria |
| --- | --- | --- |
| Tunnel health | Gateway connection status | Tunnel status is Connected. |
| Route learning | Effective routes and BGP tables | On-prem prefixes are present. |
| Path continuity | Connection troubleshoot | Probe reaches on-prem target. |

```mermaid
graph TD
    User[Cloud to On-Prem] --> Tunnel[Tunnel Status Up?]
    Tunnel -- No --> IKE[Check IKE/IPSec Config]
    Tunnel -- Yes --> BGP[BGP Session Established?]
    BGP -- No --> ASN[Verify ASNs / Peer IPs]
    BGP -- Yes --> Route[Are Routes Learned?]
```

!!! note
    Verify how far the packet travels by using `tracert` or Azure's Packet Capture tool on the Gateway.

## See Also

- [Hybrid Connectivity Basics](../platform/hybrid-connectivity-basics.md)
- [VPN and ExpressRoute Basics](../operations/vpn-and-expressroute-basics.md)
- [Hybrid Connectivity Best Practices](../best-practices/hybrid-connectivity-best-practices.md)

## Sources

- [Troubleshoot VPN Gateway connections](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-troubleshoot-site-to-site-cannot-connect)
- [Troubleshoot ExpressRoute performance and connectivity](https://learn.microsoft.com/en-us/troubleshoot/azure/expressroute/expressroute-troubleshooting-network-performance)
