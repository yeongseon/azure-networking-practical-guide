# Azure Networking Practical Guide

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

A practical guide covering Azure networking connectivity design, operations, and troubleshooting — grounded in MS Learn documentation.

## What's Inside

| Section | Description |
|---------|-------------|
| [Start Here](https://yeongseon.github.io/azure-networking-practical-guide/start-here/) | Networking overview, connectivity framing, and common architectural scenarios |
| [Platform](https://yeongseon.github.io/azure-networking-practical-guide/platform/) | Core services: VNet, DNS, routing, load balancing, and private connectivity |
| [Best Practices](https://yeongseon.github.io/azure-networking-practical-guide/best-practices/) | Production-ready design for subnetting, NSG/Firewall, and hybrid connectivity |
| [Operations](https://yeongseon.github.io/azure-networking-practical-guide/operations/) | Day-2 guide for configuring UDR, private endpoints, peering, and packet capture |
| [Tutorials](https://yeongseon.github.io/azure-networking-practical-guide/tutorials/) | Hands-on labs for hub-spoke topology, private endpoints, and WAF configuration |
| [Troubleshooting](https://yeongseon.github.io/azure-networking-practical-guide/troubleshooting/) | Diagnosis playbooks for DNS resolution, VPN gateways, and health probe failures |
| [Reference](https://yeongseon.github.io/azure-networking-practical-guide/reference/) | Quick-lookup decision guides for connectivity and routing cheatsheets |

## Focus Areas

Explore the core pillars of Azure networking included in this guide:
- **Virtual Network (VNet)**: Address space management, subnetting, and peering
- **Connectivity**: Private Endpoints, Private Link, and hybrid options (VPN, ExpressRoute)
- **Security**: Network Security Groups (NSG), Azure Firewall, and Application Gateway WAF
- **Traffic Management**: Load balancing, routing (UDR), and DNS resolution patterns
- **Observability**: Network path monitoring and packet diagnostics

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yeongseon/azure-networking-practical-guide.git

# Install MkDocs dependencies
pip install mkdocs-material mkdocs-minify-plugin

# Start local documentation server
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
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage practical guide |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service practical guide |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions practical guide |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps practical guide |
| [azure-communication-services-practical-guide](https://github.com/yeongseon/azure-communication-services-practical-guide) | Azure Communication Services practical guide |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service (AKS) practical guide |
| [azure-architecture-practical-guide](https://github.com/yeongseon/azure-architecture-practical-guide) | Azure Architecture practical guide |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring practical guide |

## Disclaimer

This is an independent community project. Not affiliated with or endorsed by Microsoft. Azure and Azure Virtual Network are trademarks of Microsoft Corporation.

## License

[MIT](LICENSE)

