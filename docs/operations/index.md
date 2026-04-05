# Operations

The Operations section provides actionable guides for deploying and managing Azure Networking resources.

| Page | Description |
| --- | --- |
| [Create VNet and Subnets](create-vnet-and-subnets.md) | Standard procedures for virtual network deployment. |
| [Configure NSG](configure-nsg.md) | Rules and best practices for Network Security Groups. |
| [Configure DNS](configure-dns.md) | Setup for Private DNS Zones and custom resolution. |
| [Configure UDR](configure-udr.md) | Routing table management and traffic steering. |
| [Connect Private Endpoints](connect-private-endpoints.md) | Securely exposing services into a VNet. |
| [Peering Basics](peering-basics.md) | Connecting virtual networks in the same or different regions. |
| [VPN and ExpressRoute](vpn-and-expressroute-basics.md) | Hybrid connectivity setup and maintenance. |
| [Monitor Network Paths](monitor-network-paths.md) | Tools for visibility into network traffic flow. |
| [Packet Capture](packet-capture-and-diagnostics.md) | Deep diagnostic procedures for complex issues. |

```mermaid
graph TD
    Start[Planning] --> VNet[Create VNet/Subnets]
    VNet --> Security[Configure NSG]
    Security --> Routing[Configure UDR]
    Routing --> Connectivity[Hybrid/Peering]
    Connectivity --> Monitoring[Monitor & Audit]
```

!!! tip
    Run changes in this order: addressing, security, routing, connectivity, then monitoring validation.

## See Also

- [Learning Path](../start-here/learning-path.md)
- [Create VNet and Subnets](./create-vnet-and-subnets.md)
- [Troubleshooting Overview](../troubleshooting/index.md)

## Sources

- [Azure Virtual Network documentation](https://learn.microsoft.com/en-us/azure/virtual-network/)
- [Azure Network Security documentation](https://learn.microsoft.com/en-us/azure/networking/security/network-security)
- [Azure Private Link documentation](https://learn.microsoft.com/en-us/azure/private-link/)
