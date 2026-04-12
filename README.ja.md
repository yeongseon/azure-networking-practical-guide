# Azure Networking 実務ガイド

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

MS Learn ドキュメントに基づいた、Azure ネットワーク接続の設計、運用、およびトラブルシューティングに関する実務ガイドです。

## スコープ

- ✅ 含まれるもの: VNet、サブネット、NSG、DNS、ルーティング、プライベート接続、ハイブリッドネットワーク、負荷分散、トラブルシューティング
- ❌ 含まれないもの: アプリケーション層プロトコルチュートリアル、サードパーティ NVA の詳細分析

## 主な内容

| セクション | 目的 |
|---------|---------|
| ここから開始 (Start Here) | ネットワーク概要、接続フレーミング、学習パス |
| プラットフォーム (Platform) | Azure ネットワークの仕組み — VNet、DNS、ルーティング、セキュリティ、ハイブリッド |
| ベストプラクティス (Best Practices) | 本番環境に対応したネットワーク設計と運用ガイドライン |
| 運用 (Operations) | ステップバイステップのネットワーク構成とモニタリング手順 |
| トラブルシューティング (Troubleshooting) | 症状ベースの接続診断と解決 |
| リファレンス (Reference) | クイックルックアップ決定ガイドとチートシート |

## コンテンツソース

すべてのコンテンツは、公式 [Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-network/) ドキュメントに基づいています。

## ローカルビルド

```bash
pip install mkdocs-material pymdown-extensions
mkdocs build --strict
mkdocs serve
```

## 関連プロジェクト

| リポジトリ | 説明 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 実務ガイド |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage 実務ガイド |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 実務ガイド |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 実務ガイド |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 実務ガイド |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service 実務ガイド |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 実務ガイド |
