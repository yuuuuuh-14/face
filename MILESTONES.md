[🌐 EN VERSION](MILESTONES_EN.md)

# 🏆 개발 마일스톤 및 트래커 (MILESTONES)

BIOMETRIC_CONTROL_CENTER(v3.5 Stable)의 기능 개발 단위별 마일스톤(목표 달성 현황)을 기로하는 문서입니다.

---

## 🏁 Milestone 1: 기반 시스템 구축 및 아키텍처 전환 [완료]
초기 레거시 구조(Docker 의존)에서 탈피하고 가볍게 실행 가능한 형태를 갖추는 단계입니다.

- **Status**: ✅ Completed
- **Epic**: Core Infrastructure
- **Task List**:
  - [x] `backend/refactor`: Docker 컨테이너 의존성 완전 제거 및 단일 로컬 프로세스로 전환
  - [x] `backend/core`: Flask를 활용한 비동기 SSE (Server-Sent Events) 프로토콜 기반 확립
  - [x] `frontend/init`: 기존 바닐라/단순 프레임워크에서 엔터프라이즈급 Angular 워크스페이스로 마이그레이션
  - [x] `config`: `requirements.txt` 내 GPU/CPU 하드웨어 호환성을 고려한 패키지 핀(Pinned) 버전 정리

---

## 🏁 Milestone 2: 얼굴 분할 및 지능형 등록 시스템 [완료]
인식의 토대가 되는 벡터 데이터의 저장 방식을 설계하고 구현하는 단계입니다.

- **Status**: ✅ Completed
- **Epic**: AI Recognition & Data Persistence
- **Task List**:
  - [x] `backend/persistence`: `data/faces.db` SQLite 기반의 영구 저장소 클래스 구현 (CRUD 지원)
  - [x] `backend/vectorize`: InsightFace 모델을 통한 512차원 특징 벡터 추출 패키징
  - [x] `backend/api`: `POST /register` 신규 인물 등록 및 벡터 직렬화 API 개발
  - [x] `frontend/modal`: 화면의 특정 타겟을 클릭하여 즉각적으로 등록을 시도하는 Angular Material Dialog UI 구현
  - [x] `backend/matching`: 두 벡터 간의 코사인 유사도(Cosine Similarity)를 계산하여 식별/비식별(UNKNOWN) 상태 판별 엔진 구축

---

## 🏁 Milestone 3: Sci-Fi UX 고도화 및 생체 정보 확장 [완료]
대시보드의 시각적 퀄리티를 최대로 끌어올리고 추가 분석 기능을 도입하는 단계입니다.

- **Status**: ✅ Completed
- **Epic**: Advanced UX & Bio-Intelligence
- **Task List**:
  - [x] `frontend/styling`: 진부한 Tailwind/Bootstrap 을 걷어내고 Pure SCSS로 네온 글로우(Neon Glow), 스캔라인(Scanlines) 이펙트 완벽 구현
  - [x] `frontend/font`: 완벽한 한국어 지원을 위한 'Noto Sans KR' 및 'Black Han Sans' 타이포그래피 설정 적용
  - [x] `frontend/dashboard`: 등록된 요원의 목록을 조회하고 원클릭 삭제 가능한 '디렉토리 패널' 구현
  - [x] `backend/ai-extension`: 기존 신원 확인 파이프라인 위에 성별(Gender) 및 예상 나이(Age) 추정 모듈 스레드 병합
  - [x] `frontend/hud-overlay`: 연령 및 성별 정보를 프로필 바운딩 박스 옆에 자연스럽게 렌더링하도록 뷰포트 레이아웃 최적화

---

## 🏁 Milestone 4: 문서화 리뉴얼 및 배포 파이프라인 최적화 [완료]
학습용 리포지토리로서의 가치를 극대화하기 위해 튜토리얼을 보강하고 안정성을 확보하는 단계입니다.

- **Status**: ✅ Completed
- **Epic**: Documentation & Final Polish
- **Task List**:
  - [x] `docs/clean`: 사용되지 않는 데드 코드 정리
  - [x] `docs/rewrite`: `WORKBOOK` 체계 리뉴얼 및 가이드 개편
  - [x] `backend/perf`: 카메라 스레드 예외 처리 및 하드웨어 가용성 체크 강화
  - [x] `docker/init`: `Dockerfile` 및 `docker-compose`를 통한 전체 스택 컨테이너화 지원
  - [x] `ci-cd/setup`: GitHub Actions를 이용한 자동화된 테스트 및 배포 파이프라인 구축

---

## 📊 요약 리포트

| 마일스톤 | 테마 | 커버리지 | 상태 |
|---------|------|---------|------|
| M1 | 기초 엔진 (Flask & Angular) | 100% | ✅ 완료 |
| M2 | 로컬 DB & 안면 매칭 | 100% | ✅ 완료 |
| M3 | Sci-Fi 인터페이스 & 한글화 | 100% | ✅ 완료 |
| M4 | 워크북 고도화 및 최적화 | 100% | ✅ 완료 |
