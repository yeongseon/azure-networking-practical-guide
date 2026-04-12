# Azure Networking 实操指南

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

基于 MS Learn 文档的 Azure 网络连接设计、运营和故障排除实操指南。

## 范围

- ✅ 包含: VNet、子网、NSG、DNS、路由、专用连接、混合网络、负载均衡、故障排除
- ❌ 不包含: 应用层协议教程、第三方 NVA 深入分析

## 主要内容

| 章节 | 目的 |
|---------|---------|
| 从这里开始 (Start Here) | 网络概述、连接框架、学习路径 |
| 平台 (Platform) | Azure 网络工作原理 — VNet、DNS、路由、安全、混合 |
| 最佳实践 (Best Practices) | 面向生产的网络设计和运营指南 |
| 运营 (Operations) | 分步网络配置和监控流程 |
| 故障排除 (Troubleshooting) | 基于症状的连接诊断和解决 |
| 参考 (Reference) | 快速查询决策指南和速查表 |

## 内容来源

所有内容基于官方 [Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-network/) 文档。

## 本地构建

```bash
pip install mkdocs-material pymdown-extensions
mkdocs build --strict
mkdocs serve
```

## 相关项目

| 仓库 | 描述 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 实操指南 |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage 实操指南 |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 实操指南 |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 实操指南 |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 实操指南 |
| [azure-aks-practical-guide](https://github.com/yeongseon/azure-aks-practical-guide) | Azure Kubernetes Service 实操指南 |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 实操指南 |
