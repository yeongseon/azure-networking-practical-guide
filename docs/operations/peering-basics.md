# Peering Basics

VNet Peering connects two virtual networks with low latency.

| Property | Description | Note |
| --- | --- | --- |
| Local VNet | The VNet where peering is configured. | Must not overlap CIDR. |
| Remote VNet | The target VNet for connection. | Can be in any region. |
| Allow Forwarded | Allows traffic from other peers. | Needed for Hub-Spoke. |
| Gateway Transit | Allows peer to use local gateway. | Only one side can use it. |

```mermaid
graph LR
    VNetA[VNet A] -- Peering -- VNetB[VNet B]
    VNetB -- Peering -- VNetC[VNet C]
    VNetA -. No Direct Access .- VNetC
```

!!! note
    Peering is non-transitive by default. To reach VNet C from VNet A via VNet B, you need an NVA or VPN Gateway.

## Sources

- [Virtual network peering overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview)
- [Create, change, or delete a virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)
