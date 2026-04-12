# Azure Networking 실무 가이드

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

MS Learn 문서를 기반으로 한 Azure 네트워킹 연결 설계, 운영 및 트러블슈팅을 다루는 실무 가이드입니다.

## 범위

- ✅ 포함: VNet, 서브넷, NSG, DNS, 라우팅, 프라이빗 연결, 하이브리드 네트워킹, 부하 분산, 트러블슈팅
- ❌ 제외: 애플리케이션 계층 프로토콜 튜토리얼, 서드파티 NVA 심화 분석

## 주요 내용

| 섹션 | 목적 |
|---------|---------|
| 시작하기 (Start Here) | 네트워킹 개요, 연결 프레이밍, 학습 경로 |
| 플랫폼 (Platform) | Azure 네트워킹 작동 원리 — VNet, DNS, 라우팅, 보안, 하이브리드 |
| 베스트 프랙티스 (Best Practices) | 운영 환경에 적합한 네트워크 설계 및 운영 가이드라인 |
| 운영 (Operations) | 단계별 네트워크 구성 및 모니터링 절차 |
| 트러블슈팅 (Troubleshooting) | 증상 기반 연결 진단 및 해결 |
| 참조 (Reference) | 빠른 조회 의사 결정 가이드 및 치트시트 |

## 콘텐츠 소스

모든 콘텐츠는 공식 [Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-network/) 문서를 기반으로 합니다.

## 로컬 빌드

```bash
pip install mkdocs-material pymdown-extensions
mkdocs build --strict
mkdocs serve
```

## 관련 프로젝트

| 저장소 | 설명 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 실무 가이드 |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage 실무 가이드 |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 실무 가이드 |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 실무 가이드 |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 실무 가이드 |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service 실무 가이드 |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 실무 가이드 |
