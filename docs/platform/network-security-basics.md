# Network Security Basics

Azure network security is based on a zero-trust model, implementing multiple layers of defense to protect resources from unauthorized access.

| Control | Layer | Scope | Key Feature |
| --- | --- | --- | --- |
| NSG | Layer 3/4 | Subnet/NIC | Stateful filtering. |
| Azure Firewall | Layer 3/4/7 | Regional | FQDN filtering. |
| WAF | Layer 7 | Global/Regional | OWASP protection. |
| DDoS Protection | Layer 3/4 | Global | Traffic scrubbing. |

```mermaid
graph LR
    Internet[Internet] --> DDoS[DDoS Protection]
    DDoS --> AFW[Azure Firewall]
    AFW --> NSG[Subnet NSG]
    NSG --> VM[Target Resource]
    WAF[WAF / App Gateway] -.-> AFW
```

!!! note
    NSG rules are processed in priority order (lowest number first). Once a match is found, no further rules are processed. Default rules are always at the end with the highest numbers.

## Security Control Placement

| Placement | Primary Control | Typical Outcome |
| --- | --- | --- |
| Edge ingress | DDoS + WAF | Reduced attack surface |
| Network transit | Azure Firewall | Centralized policy enforcement |
| Workload subnet | NSG | Least-privilege east-west filtering |

## See Also

- [NSG and Firewall Best Practices](../best-practices/nsg-and-firewall-best-practices.md)
- [Configure Network Security Groups](../operations/configure-nsg.md)
- [NSG vs UDR vs Firewall](../troubleshooting/nsg-vs-udr-vs-firewall.md)

## Sources

- [Azure network security overview](https://learn.microsoft.com/en-us/azure/networking/fundamentals/networking-overview#network-security)
- [Network security groups overview](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)
