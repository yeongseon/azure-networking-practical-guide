# Azure Networking 实操指南

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

📘 文档网站: <https://yeongseon.github.io/azure-networking-practical-guide/>

[![Docs](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/docs.yml/badge.svg)](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/docs.yml)
[![CI](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/validate-content-sources.yml/badge.svg)](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/validate-content-sources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

基于 MS Learn 文档的 Azure 网络连接设计、运营和故障排除实操指南。

## 包含内容

| 章节 | 说明 | 状态 |
|---------|-------------|--------|
| [从这里开始](https://yeongseon.github.io/azure-networking-practical-guide/start-here/) | 网络概述、连接框架和常见的架构场景 | 全面 |
| [平台](https://yeongseon.github.io/azure-networking-practical-guide/platform/) | 核心服务：VNet、DNS、路由、负载均衡和专用连接 | 全面 |
| [最佳实践](https://yeongseon.github.io/azure-networking-practical-guide/best-practices/) | 子网、NSG/防火墙和混合连接的面向量产的设计 | 全面 |
| [运营](https://yeongseon.github.io/azure-networking-practical-guide/operations/) | 用于配置 UDR、专用终结点、对等互连和数据包捕获的 Day-2 指南 | 全面 |
| [教程](https://yeongseon.github.io/azure-networking-practical-guide/tutorials/) | 用于中心辐射型拓扑、专用终结点和 WAF 配置的手操实验室 | 全面 |
| [故障排除](https://yeongseon.github.io/azure-networking-practical-guide/troubleshooting/) | 用于 DNS 解析、VPN 网关和运行状况探测失败的诊断手册 | 已发布 |
| [参考](https://yeongseon.github.io/azure-networking-practical-guide/reference/) | 用于连接和路由速查表的快速查询决策指南 | 全面 |

**状态说明**: **实验室验证** = 全面的内容 + 可重复的实验室验证了指南 · **全面** = 完整章节，经过 MSLearn 验证，面向量产 · **已发布** = 核心内容已就绪，仍在中扩展 · **进行中** = 部分内容，正在积极开发 · **计划中** = 占位符，内容尚未开始

## 重点领域

探索本指南中包含的 Azure 网络的核心支柱：
- **虚拟网络 (VNet)**：地址空间管理、子网划分和对等互连
- **连接性**：专用终结点、Private Link 和混合选项 (VPN, ExpressRoute)
- **安全性**：网络安全组 (NSG)、Azure 防火墙和应用程序网关 WAF
- **流量管理**：负载均衡、路由 (UDR) 和 DNS 解析模式
- **可观测性**：网络路径监控和数据包诊断

## 快速入门

```bash
git clone https://github.com/yeongseon/azure-networking-practical-guide.git
cd azure-networking-practical-guide

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt

mkdocs serve
```

访问 `http://127.0.0.1:8000` 以在本地浏览文档。

## 参与贡献

欢迎参与贡献！有关以下内容，请参阅我们的 [贡献指南](https://yeongseon.github.io/azure-networking-practical-guide/contributing/)：

- 仓库结构和内容组织
- 文档模板和编写标准
- 本地开发设置和构建验证
- 拉取请求流程

## 相关项目

| 仓库 | 描述 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 实操指南 |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking 实操指南 |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage 实操指南 |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 实操指南 |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 实操指南 |
| [azure-communication-services-practical-guide](https://github.com/yeongseon/azure-communication-services-practical-guide) | Azure Communication Services 实操指南 |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 实操指南 |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service (AKS) 实操指南 |
| [azure-architecture-practical-guide](https://github.com/yeongseon/azure-architecture-practical-guide) | Azure Architecture 实操指南 |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 实操指南 |

## 免责声明

这是一个独立的社区项目。不隶属于 Microsoft，也不受其认可。Azure 和 Azure Virtual Network 是 Microsoft Corporation 的商标。

## 许可证

[MIT](LICENSE)
