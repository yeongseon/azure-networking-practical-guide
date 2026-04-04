# VNet and Subnet Basics

Virtual Networks (VNets) are the fundamental building block for your private network in Azure. They provide isolation, segmentation, and communication for your cloud resources.

| Property | Description | Scope |
| --- | --- | --- |
| Address Space | CIDR block defining the network range. | VNet |
| Region | Location where the VNet resides. | Regional |
| Peering | Connects two VNets via Azure backbone. | Global/Regional |
| DNS Settings | Specifies Azure or custom DNS servers. | VNet |

| Subnet Type | Common Purpose | Mandatory Name |
| --- | --- | --- |
| Default | General workload hosting (VMs, etc). | N/A |
| Gateway | Site-to-Site VPN or ExpressRoute. | GatewaySubnet |
| Bastion | Secure RDP/SSH management access. | AzureBastionSubnet |
| Firewall | Centralized network security. | AzureFirewallSubnet |
| Private Endpoint | Private access to PaaS services. | N/A |

```mermaid
graph TD
    VNet[Virtual Network /16] --> S1[Web Subnet /24]
    VNet --> S2[App Subnet /24]
    VNet --> S3[DB Subnet /24]
    VNet --> S4[GatewaySubnet /27]
    S1 --> VM1[Web VM]
    S2 --> VM2[App VM]
    S3 --> PE[Private Endpoint]
```

## Sources

- [Azure Virtual Network concepts](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
- [Plan and design Azure Virtual Networks](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm)
