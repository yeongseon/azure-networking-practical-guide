# Azure Networking Practical Guide

A practical guide covering Azure networking connectivity design, operations, and troubleshooting — grounded in MS Learn documentation.

## Scope

- ✅ Included: VNet, subnet, NSG, DNS, routing, private connectivity, hybrid networking, load balancing, troubleshooting
- ❌ Excluded: Application-layer protocol tutorials, third-party NVA deep dives

## Sections

| Section | Purpose |
|---------|---------|
| Start Here | Networking overview, connectivity framing, reading paths |
| Platform | How Azure networking works — VNet, DNS, routing, security, hybrid |
| Best Practices | Production-ready network design and operational guidelines |
| Operations | Step-by-step network configuration and monitoring procedures |
| Troubleshooting | Symptom-based connectivity diagnosis and resolution |
| Reference | Quick-lookup decision guides and cheatsheets |

## Content Source

All content is grounded in official [Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-network/) documentation.

## Local Build

```bash
pip install mkdocs-material pymdown-extensions
mkdocs build --strict
mkdocs serve
```
