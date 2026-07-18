# Azure Networking 실무 가이드

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

📘 문서 사이트: <https://yeongseon.github.io/azure-networking-practical-guide/>

[![Docs](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/docs.yml/badge.svg)](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/docs.yml)
[![CI](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/validate-content-sources.yml/badge.svg)](https://github.com/yeongseon/azure-networking-practical-guide/actions/workflows/validate-content-sources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

MS Learn 문서를 기반으로 Azure 네트워킹 연결 설계, 운영 및 트러블슈팅을 다루는 실무 가이드입니다.

## 주요 내용

| 섹션 | 설명 | 상태 |
|---------|-------------|--------|
| [시작하기](https://yeongseon.github.io/azure-networking-practical-guide/start-here/) | 네트워킹 개요, 연결 프레이밍 및 일반적인 아키텍처 시나리오 | 종합적 |
| [플랫폼](https://yeongseon.github.io/azure-networking-practical-guide/platform/) | 핵심 서비스: VNet, DNS, 라우팅, 부하 분산 및 프라이빗 연결 | 종합적 |
| [베스트 프랙티스](https://yeongseon.github.io/azure-networking-practical-guide/best-practices/) | 서브네팅, NSG/Firewall 및 하이브리드 연결을 위한 프로덕션 준비 설계 | 종합적 |
| [운영](https://yeongseon.github.io/azure-networking-practical-guide/operations/) | UDR, 프라이빗 엔드포인트, 피어링 및 패킷 캡처 구성을 위한 Day-2 가이드 | 종합적 |
| [튜토리얼](https://yeongseon.github.io/azure-networking-practical-guide/tutorials/) | 허브-앤-스포크 토폴로지, 프라이빗 엔드포인트 및 WAF 구성을 위한 실습 | 종합적 |
| [트러블슈팅](https://yeongseon.github.io/azure-networking-practical-guide/troubleshooting/) | DNS 확인, VPN 게이트웨이 및 상태 프로브 실패를 위한 진단 플레이북 | 게시됨 |
| [참조](https://yeongseon.github.io/azure-networking-practical-guide/reference/) | 연결 및 라우팅 치트 시트를 위한 빠른 조회 의사 결정 가이드 | 종합적 |

**상태 범례**: **실습 검증됨(Lab-validated)** = 종합적인 내용 + 재현 가능한 실습으로 가이드 검증됨 · **종합적(Comprehensive)** = 전체 섹션 완료, MSLearn 검증됨, 프로덕션 준비됨 · **게시됨(Published)** = 핵심 콘텐츠 배치됨, 계속 확장 중 · **진행 중(In progress)** = 부분적인 콘텐츠, 활발히 개발 중 · **계획됨(Planned)** = 플레이스홀더, 콘텐츠 아직 시작되지 않음

## 집중 분야

이 가이드에 포함된 Azure 네트워킹의 핵심 요소들을 살펴보세요:
- **가상 네트워크 (VNet)**: 주소 공간 관리, 서브네팅 및 피어링
- **연결성**: 프라이빗 엔드포인트, 프라이빗 링크 및 하이브리드 옵션 (VPN, ExpressRoute)
- **보안**: 네트워크 보안 그룹 (NSG), Azure Firewall 및 Application Gateway WAF
- **트래픽 관리**: 부하 분산, 라우팅 (UDR) 및 DNS 확인 패턴
- **관찰성**: 네트워크 경로 모니터링 및 패킷 진단

## 빠른 시작

```bash
git clone https://github.com/yeongseon/azure-networking-practical-guide.git
cd azure-networking-practical-guide

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt

mkdocs serve
```

로컬에서 문서를 찾아보려면 `http://127.0.0.1:8000`에 접속하세요.

## 기여하기

기여는 언제나 환영합니다! 다음 사항에 대해서는 [기여 가이드](https://yeongseon.github.io/azure-networking-practical-guide/contributing/)를 참조하세요:

- 저장소 구조 및 콘텐츠 구성
- 문서 템플릿 및 작성 표준
- 로컬 개발 설정 및 빌드 검증
- 풀 요청 프로세스

## 관련 프로젝트

| 저장소 | 설명 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 실무 가이드 |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking 실무 가이드 |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage 실무 가이드 |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 실무 가이드 |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 실무 가이드 |
| [azure-communication-services-practical-guide](https://github.com/yeongseon/azure-communication-services-practical-guide) | Azure Communication Services 실무 가이드 |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 실무 가이드 |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service (AKS) 실무 가이드 |
| [azure-architecture-practical-guide](https://github.com/yeongseon/azure-architecture-practical-guide) | Azure Architecture 실무 가이드 |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 실무 가이드 |

## 면책 조항

본 프로젝트는 독립적인 커뮤니티 프로젝트입니다. Microsoft와 제휴하거나 Microsoft의 보증을 받지 않았습니다. Azure 및 Azure Virtual Network는 Microsoft Corporation의 상표입니다.

## 라이선스

[MIT](LICENSE)
