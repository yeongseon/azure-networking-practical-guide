# DNS Resolution Failures

Addressing naming resolution issues in VNets.

| Symptom | Probable Cause | Resolution |
| --- | --- | --- |
| Resolves to Public IP | Missing Private Zone Link. | Add VNet Link to Zone. |
| NXDOMAIN | Record not in Zone. | Add/Verify Record. |
| Timeout | DNS Port 53 Blocked. | Check NSG / Firewall. |
| Incorrect IP | Overlapping DNS Zones. | Review Zone precedence. |

```mermaid
graph TD
    Client[Query Name] --> Server[Check DNS Server IP]
    Server -- 168.63.129.16 --> Azure[Azure DNS Used]
    Server -- Other --> Custom[Custom DNS Used]
    Azure --> Link[Is VNet Linked to Zone?]
    Custom --> Forward[Check Forwarding Rule]
```

!!! note
    Check which DNS server the client is using with `ipconfig /all` or `cat /etc/resolv.conf`.

## Sources

- [Azure DNS troubleshooting guide](https://learn.microsoft.com/en-us/azure/dns/dns-troubleshoot)
- [Troubleshoot Private DNS Zones](https://learn.microsoft.com/en-us/azure/dns/private-dns-troubleshoot-guide)
