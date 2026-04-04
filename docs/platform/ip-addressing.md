# IP Addressing

Azure uses a flexible IP addressing scheme for both private and public communications. Public IPs enable external access, while private IPs handle internal resource connectivity.

| IP Type | Allocation | Lifecycle | Use Case |
| --- | --- | --- | --- |
| Private Dynamic | DHCP from subnet. | Freed on VM stop/deallocate. | General compute. |
| Private Static | User-defined from subnet. | Persists until deleted. | Domain controllers, DNS servers. |
| Public Dynamic | Assigned from Azure pool. | Changes on resource restart. | Basic web services. |
| Public Static | Fixed from Azure pool. | Persists across restarts. | VPN gateways, Firewalls. |

```mermaid
graph TD
    A[New IP Request] --> B{IP Type?}
    B -->|Public| C{SKU?}
    B -->|Private| D[Assigned via DHCP]
    C -->|Standard| E[Static Only]
    C -->|Basic| F[Dynamic/Static]
    E --> G[Resource (NIC/LB)]
    F --> G
    D --> G
```

!!! note
    Public IP Basic SKU is being retired. It's recommended to use Standard SKU for all new deployments as it provides zone-redundancy and high availability.

## See Also

- [VNet and Subnet Basics](vnet-and-subnet-basics.md)
- [DNS Basics](dns-basics.md)
- [Azure Networking Components](../reference/azure-networking-components.md)

## Sources

- [Public IP address types and methods](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)
- [Private IP addresses in Azure](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/private-ip-addresses)
