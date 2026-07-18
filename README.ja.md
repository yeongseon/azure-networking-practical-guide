# Azure Networking 実務ガイド

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

📘 ドキュメントサイト: <https://yeongseon.github.io/azure-networking-practical-guide/>

[![Docs](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/docs.yml/badge.svg)](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/docs.yml)
[![CI](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/validate-content-sources.yml/badge.svg)](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/validate-content-sources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

MS Learn ドキュメントに基づいた、Azure ネットワーク接続の設計、運用、およびトラブルシューティングに関する実務ガイドです.

## 主な内容

| セクション | 説明 | 状態 |
|---------|-------------|--------|
| [ここから開始](https://yeongseon.github.io/azure-networking-practical-guide/start-here/) | ネットワーク概要、接続フレーミング、および一般的なアーキテクチャシナリオ | 総合的 |
| [プラットフォーム](https://yeongseon.github.io/azure-networking-practical-guide/platform/) | コアサービス: VNet、DNS、ルーティング、負荷分散、およびプライベート接続 | 総合的 |
| [ベストプラクティス](https://yeongseon.github.io/azure-networking-practical-guide/best-practices/) | サブネット、NSG/Firewall、およびハイブリッド接続のための本番環境に対応した設計 | 総合적 |
| [運用](https://yeongseon.github.io/azure-networking-practical-guide/operations/) | UDR、プライベートエンドポイント、ピアリング、およびパケットキャプチャ構成のための Day-2 ガイド | 総合的 |
| [チュートリアル](https://yeongseon.github.io/azure-networking-practical-guide/tutorials/) | ハブ・アンド-スポークトポロジ、プライベートエンドポイント、および WAF 構成のためのハンズオンラボ | 総合的 |
| [トラブルシューティング](https://yeongseon.github.io/azure-networking-practical-guide/troubleshooting/) | DNS 解決、VPN ゲートウェイ、および正常性プローブ失敗のための診断プレイブック | 公開済み |
| [リファレンス](https://yeongseon.github.io/azure-networking-practical-guide/reference/) | 接続およびルーティングのチートシートのためのクイックルックアップ決定ガイド | 総合的 |

**状態の凡例**: **ラボ検証済み(Lab-validated)** = 総合的な内容 + 再現可能なラボによりガイダンスを検証済み · **総合的(Comprehensive)** = 全セクション完了、MSLearn 検証済み、本番環境対応 · **公開済み(Published)** = コアコンテンツ配置済み、拡張中 · **進行中(In progress)** = 一部のコンテンツ、活発に開発中 · **計画中(Planned)** = プレースホルダー、コンテンツ未開始

## 注力分野

このガイドに含まれる Azure ネットワークの主要な柱を探索してください:
- **Virtual Network (VNet)**: アドレス空間管理、サブネッティング、およびピアリング
- **接続性**: プライベートエンドポイント、プライベートリンク、およびハイブリッドオプション (VPN, ExpressRoute)
- **セキュリティ**: ネットワークセキュリティグループ (NSG)、Azure Firewall、および Application Gateway WAF
- **トラフィック管理**: 負荷分散、ルーティング (UDR)、および DNS 解決パターン
- **オブザーバビリティ**: ネットワークパスモニタリングおよびパケット診断

## クイックスタート

```bash
git clone https://github.com/yeongseon/azure-networking-practical-guide.git
cd azure-networking-practical-guide

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt

mkdocs serve
```

ローカルでドキュメントを閲覧するには `http://127.0.0.1:8000` にアクセスしてください。

## 貢献する

貢献はいつでも歓迎します！以下の詳細については [貢献ガイド](https://yeongseon.github.io/azure-networking-practical-guide/contributing/) を参照してください:

- リポジトリ構造とコンテンツ構成
- ドキュメントテンプレートと執筆基準
- ローカル開発環境のセットアップとビルド検証
- プルリクエストプロセス

## 関連プロジェクト

| リポジトリ | 説明 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 実務ガイド |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking 実務ガイド |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage 実務ガイド |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 実務ガイド |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 実務ガイド |
| [azure-communication-services-practical-guide](https://github.com/yeongseon/azure-communication-services-practical-guide) | Azure Communication Services 実務ガイド |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 実務ガイド |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service 実務ガイド |
| [azure-architecture-practical-guide](https://github.com/yeongseon/azure-architecture-practical-guide) | Azure Architecture 実务ガイド |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 実務ガイド |

## 免責事項

これは独立したコミュニティプロジェクトです。Microsoft との提携や承認はありません。Azure および Azure Virtual Network は Microsoft Corporation の商標です。

## ライセンス

[MIT](LICENSE)
