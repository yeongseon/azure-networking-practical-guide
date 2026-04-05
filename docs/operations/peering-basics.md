# Peering Basics

VNet Peering connects two virtual networks with low latency.

| Property | Description | Note |
| --- | --- | --- |
| Local VNet | The VNet where peering is configured. | Must not overlap CIDR. |
| Remote VNet | The target VNet for connection. | Can be in any region. |
| Allow Forwarded | Allows traffic from other peers. | Needed for Hub-Spoke. |
| Gateway Transit | Allows peer to use local gateway. | Only one side can use it. |

| Verification | Checkpoint | Expected Result |
| --- | --- | --- |
| Peering state | Both peerings show Connected | Bidirectional reachability ready. |
| Address space | No overlap between VNets | Route propagation succeeds. |
| Effective routes | Peer prefixes visible on NIC | Traffic can target remote CIDR. |

```mermaid
graph LR
    VNetA[VNet A] -- Peering -- VNetB[VNet B]
    VNetB -- Peering -- VNetC[VNet C]
    VNetA -. No Direct Access .- VNetC
```

!!! note
    Peering is not transitive. For A-B-C Azure VNet chains, use direct peering between A and C, or service chaining via NVA/Azure Firewall in hub B.

## See Also

- [How Azure Networking Works](../platform/how-azure-networking-works.md)
- [Peering and Routing Issues](../troubleshooting/peering-and-routing-issues.md)
- [Configure UDR](./configure-udr.md)

## Sources

- [Virtual network peering overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview)
- [Create, change, or delete a virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)
