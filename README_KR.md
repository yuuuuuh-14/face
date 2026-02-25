[🌐 EN VERSION](README.md)
[![BCC CI](https://github.com/yuuuuuh14/face/actions/workflows/bcc-ci.yml/badge.svg)](https://github.com/yuuuuuh14/face/actions/workflows/bcc-ci.yml)

# 👁️ BIOMETRIC_CONTROL_CENTER (BCC)
**Sci-Fi HUD 기반 로컬 실시간 얼굴 인식 시스템 v3.5 Stable**

BIOMETRIC_CONTROL_CENTER(이하 BCC)는 최신 머신러닝 모델과 모던 웹 기술을 융합하여 구축된 **오프라인/로컬 전용 생체 인식 대시보드**입니다.
사이버펑크 무드의 미려한 UI/UX를 제공하며, 로컬 네이티브 환경과 Docker 컨테이너 환경을 모두 지원합니다.

---

## ✨ 핵심 기능 (Features)
- 🎯 **고성능 얼굴 인식**: InsightFace (`antelopev2`) 기반의 512차원 특징 벡터 추출 및 코사인 유사도 매칭.
- 🛡️ **안티-스푸핑 (Liveness Detection)**: 엣지 검출(Laplacian Variance)을 통한 심플하고 강력한 위변조(사진/스크린) 방어 로직.
- 📜 **출입 접근 통합 보존(DB Log Dashboard)**: 얼굴 감지 및 스푸핑 통과 여부를 SQLiteDB에 타임스탬프와 함께 자동 영구 기록.
- 🐳 **Docker 지원**: `docker-compose`를 통한 전체 스택 컨테이너화로 환경 일관성 및 간편한 배포 지원.
- ⚙️ **CI/CD 파이프라인**: GitHub Actions를 통한 백엔드(Pytest) 및 프론트엔드(Vitest) 자동 테스트로 코드 품질 유지.
- 🖥️ **Sci-Fi HUD 인터페이스**: Angular Material과 SCSS로 구현된 사이버네틱 글로우 효과 및 한국어 타이포그래피.
- ⚡ **양방향 실시간 통신**: MJPEG 비디오 스트리밍과 SSE(Server-Sent Events)를 결합하여 지연 없는 오버레이 제공.

---

## 🛠️ 기술 스택 (Tech Stack)

### Backend (Python 3.11+)
- **Framework**: Flask (REST API + SSE)
- **AI / Computer Vision**: OpenCV, InsightFace (ArcFace), ONNXRuntime
- **Storage**: 초경량 SQLite Database (`data/faces.db`)

### Frontend (Node.js 18+)
- **Framework**: Angular v15+ (Standalone Components 기반)
- **Styling**: Angular Material + Custom SCSS (Sci-Fi 테마)

---

## 🚀 빠른 시작 가이드 (Quick Start)

BCC는 **대화형 통합 실행 스크립트**를 제공합니다. 명령어를 입력하면 **Docker** 사용 여부를 선택할 수 있습니다.

### 🍏 macOS / 🐧 Linux 환경
```bash
./run.sh
# Prompt: "🐳 Do you want to run with Docker? (y/N)"
```

### 🪟 Windows 환경
```cmd
run.bat
:: Prompt: "🐳 Do you want to run with Docker? (y/N)"
```

> **성공 여부 확인:**
> 브라우저가 열리면 `http://localhost:4200` 에 접속하여 카메라 권한을 허용하십시오.
> 백엔드 데이터 스트림 및 **자동화된 API API 문서(Swagger)**는 `http://localhost:8001/` 에서 확인하실 수 있습니다. (환경에 따라 `faces.db` 혹은 `test_faces.db`가 사용됩니다.)

---

## 📚 문서 아카이브 (Documentation)
BCC 프로젝트를 깊이 이해하고 싶다면 아래 문서들을 순서대로 읽어보세요.

- 🗺️ **[프로젝트 기획 및 구조 (PROJECT_PLAN.md)](PROJECT_PLAN.md)** - 아키텍처 및 페이즈별 진척도
- 🎯 **[개발 마일스톤 (MILESTONES.md)](MILESTONES.md)** - 핵심 개발 내역 및 이슈 트래킹
- 📖 **[학습 워크북 (docs/WORKBOOK.md)](docs/WORKBOOK.md)** - 시스템의 기반 원리와 기술적 디테일을 설명하는 종합 가이드북

---
**License**: LGPL v2.1 
**Status**: Active / Supported
