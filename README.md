# Azure Networking Practical Guide

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

📘 Documentation site: <https://yeongseon.github.io/azure-networking-practical-guide/>

[![Docs](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/docs.yml/badge.svg)](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/docs.yml)
[![CI](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/validate-content-sources.yml/badge.svg)](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/validate-content-sources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A practical guide covering Azure networking connectivity design, operations, and troubleshooting — grounded in MS Learn documentation.

## What's Inside

| Section | Description | Status |
|---------|-------------|--------|
| [Start Here](https://yeongseon.github.io/azure-networking-practical-guide/start-here/) | Networking overview, connectivity framing, and common architectural scenarios | Comprehensive |
| [Platform](https://yeongseon.github.io/azure-networking-practical-guide/platform/) | Core services: VNet, DNS, routing, load balancing, and private connectivity | Comprehensive |
| [Best Practices](https://yeongseon.github.io/azure-networking-practical-guide/best-practices/) | Production-ready design for subnetting, NSG/Firewall, and hybrid connectivity | Comprehensive |
| [Operations](https://yeongseon.github.io/azure-networking-practical-guide/operations/) | Day-2 guide for configuring UDR, private endpoints, peering, and packet capture | Comprehensive |
| [Tutorials](https://yeongseon.github.io/azure-networking-practical-guide/tutorials/) | Hands-on labs for hub-spoke topology, private endpoints, and WAF configuration | Comprehensive |
| [Troubleshooting](https://yeongseon.github.io/azure-networking-practical-guide/troubleshooting/) | Diagnosis playbooks for DNS resolution, VPN gateways, and health probe failures | Published |
| [Reference](https://yeongseon.github.io/azure-networking-practical-guide/reference/) | Quick-lookup decision guides for connectivity and routing cheatsheets | Comprehensive |

**Status legend**: **Lab-validated** = Comprehensive + reproducible labs prove the guidance · **Comprehensive** = Full section, MSLearn-verified, production-ready · **Published** = Core content in place, still expanding · **In progress** = Partial content, active development · **Planned** = Placeholder, content not yet started

## Focus Areas

Explore the core pillars of Azure networking included in this guide:
- **Virtual Network (VNet)**: Address space management, subnetting, and peering
- **Connectivity**: Private Endpoints, Private Link, and hybrid options (VPN, ExpressRoute)
- **Security**: Network Security Groups (NSG), Azure Firewall, and Application Gateway WAF
- **Traffic Management**: Load balancing, routing (UDR), and DNS resolution patterns
- **Observability**: Network path monitoring and packet diagnostics

## Quick Start

```bash
git clone https://github.com/yeongseon/azure-networking-practical-guide.git
cd azure-networking-practical-guide

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt

mkdocs serve
```

Visit `http://127.0.0.1:8000` to browse the documentation locally.

## Contributing

Contributions welcome! Please see our [Contributing Guide](https://yeongseon.github.io/azure-networking-practical-guide/contributing/) for:

- Repository structure and content organization
- Document templates and writing standards
- Local development setup and build validation
- Pull request process

## Related Projects

| Repository | Description |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines practical guide |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking practical guide |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage practical guide |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service practical guide |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions practical guide |
| [azure-communication-services-practical-guide](https://github.com/yeongseon/azure-communication-services-practical-guide) | Azure Communication Services practical guide |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps practical guide |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service (AKS) practical guide |
| [azure-architecture-practical-guide](https://github.com/yeongseon/azure-architecture-practical-guide) | Azure Architecture practical guide |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring practical guide |

## Disclaimer

This is an independent community project. Not affiliated with or endorsed by Microsoft. Azure and Azure Virtual Network are trademarks of Microsoft Corporation.

## License

[MIT](LICENSE)
