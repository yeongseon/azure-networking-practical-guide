# Outbound Connectivity Issues

Resolving failures when workloads attempt to reach external targets.

| Cause | Indicator | Resolution |
| --- | --- | --- |
| SNAT Exhaustion | Load Balancer metrics high. | Increase Outbound Ports. |
| UDR 0.0.0.0/0 | Packet reaches NVA. | Check NVA/Firewall Rules. |
| NSG Outbound Deny | IP Flow Verify fails. | Update Outbound Rule. |
| Public IP missing | Internet access fails. | Associate Nat Gateway / Public IP. |

| Isolation Test | Command / Tool | Expected Signal |
| --- | --- | --- |
| IP-only egress | `Test-NetConnection 1.1.1.1 -Port 443` | TCP reachable by IP. |
| Name-based egress | `nslookup` then TCP test | DNS and path both succeed. |
| Route decision | Next Hop diagnostic | Correct egress device selected. |

```mermaid
graph TD
    Source[VM/App] --> Route[Check 0.0.0.0/0 Route]
    Route -- Default --> VNet[VNet-to-Internet]
    Route -- UDR --> NVA[Send to Firewall]
    VNet --> SNAT[SNAT Port Check]
    NVA --> Rules[NVA Filter Rules]
```

!!! note
    Separate TCP connection failures from DNS failures. If you can `ping 8.8.8.8` but not `ping google.com`, your issue is DNS.

## See Also

- [Routing Basics](../platform/routing-basics.md)
- [Configure UDR](../operations/configure-udr.md)
- [NSG vs UDR vs Firewall](./nsg-vs-udr-vs-firewall.md)

## Sources

- [Troubleshoot outbound connectivity](https://learn.microsoft.com/en-us/azure/load-balancer/troubleshoot-outbound-connection)
- [Outbound rules for Azure Load Balancer](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-outbound-rules-overview)
