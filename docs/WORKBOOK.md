[🌐 EN VERSION](WORKBOOK_EN.md)

# 📚 BIOMETRIC_CONTROL_CENTER (BCC) 학습 워크북

본 워크북은 BCC 프로젝트의 소스코드를 분석하고 구조를 이해하기 위한 **단계별 공식 가이드**입니다.
단순히 코드를 복사하는 것을 넘어, **'왜 이것을 이 기술로 만들었는가(Why)'** 에 대한 설계 철학을 심도 있게 다룹니다.

## 🗂️ 챕터 디렉토리 (Index)

루트 목차입니다. 각 항목을 클릭하여 상세 학습 문서(`docs/workbook/*.md`)로 진입할 수 있습니다.

---

### [Part 1] 프로젝트의 본질과 기반 지식
1. **[01-intro.md](./workbook/01-intro.md) (서론)**
   - 시스템의 존재 이유, Sci-Fi HUD 디자인에 담긴 철학과 로컬 퍼스트 운영의 당위성
2. **[02-first-principles.md](./workbook/02-first-principles.md) (컴퓨터 비전과 기반 원리)**
   - MJPEG 스트리밍의 본질, 왜 단순 이미지 프레임 전송에 의존하는가
   - 얼굴 '감지(Detection)' 와 '인식(Recognition)'의 명확한 기술적 차이

---

### [Part 2] 아키텍처와 분산 계층망
3. **[03-project-structure.md](./workbook/03-project-structure.md) (구조 분석)**
   - 프론트(Angular) ↔ 백엔드(Flask) ↔ 데이터(JSON) 에 이르는 이벤트 통신 파이프라인
4. **[04-backend-stack.md](./workbook/04-backend-stack.md) (AI 스레딩 및 백엔드)**
   - 파이썬 멀티스레딩/GIL 한계와 프레임 지연율 극복 수단
   - 코사인 유사도 연산 메커니즘 뜯어보기
5. **[05-frontend-stack.md](./workbook/05-frontend-stack.md) (렌더링 및 HUD 뷰어)**
   - Angular 단일 페이지의 캔버스 렌더링 최적화 기법 (Change Detection 튜닝)
   - 글로우(Glow) 효과의 부하를 최소화하는 CSS 애니메이션 테크닉
6. **[06-database-design.md](./workbook/06-database-design.md) (영구 저장 체계 설계)**
   - 무거운 RDBMS를 버리고 단일 `JSON` 객체 파일 스토리지를 선택한 이유 및 Trade-off 분석

---

### [Part 3] 개발 역사 및 협업
7. **[07-deployment.md](./workbook/07-deployment.md) (환경 격리와 구동 원리)**
   - 리눅스/윈도우 가상 환경 패러다임 이해
8. **[08-phase-guide.md](./workbook/08-phase-guide.md) (마일스톤 회고록)**
   - 프로젝트 릴리즈 Phase 1 ~ Phase 4 에 걸친 진화 과정
9. **[09-ai-instructions.md](./workbook/09-ai-instructions.md) (생성형 AI 컨텍스트 활용)**
   - 차세대 코딩을 위해 LLM(Claude, ChatGPT, Gemini 등)에게 시스템 맥락을 어떻게 잘 설명할 것인가

---

### [Part 4] 운영 지침 (Ops)
10. **[10-troubleshooting.md](./workbook/10-troubleshooting.md) (장애 대응 매뉴얼)**
    - 흔히 발생하는 파이썬 의존성 지옥 해결 방법, 카메라 소켓 에러 대처법
11. **[11-project-tips.md](./workbook/11-project-tips.md) (프로젝트 팁 & 트릭)**
    - 코드의 확장 가능성과 유지 보수성 확보론
12. **[12-quick-reference.md](./workbook/12-quick-reference.md) (치트 시트)**
    - Angular, Flask, Yarn, Pip 주요 명령어 모음집
13. **[13-final-advice.md](./workbook/13-final-advice.md) (결어)**
    - 아키텍트를 위한 마지막 사상적 조언

---

## 🛤️ 독자 유형별 권장 학습 경로

- **'나는 그냥 이 코드를 내 맘대로 뜯어 고치고 싶다' (신속 해킹 모드)**
  - `03-project-structure.md` ➡️ `10-troubleshooting.md` ➡️ `12-quick-reference.md`
- **'왜 도커를 안쓰고 이렇게 개발했는지 아키텍처를 알고 싶다' (설계자 모드)**
  - `01-intro.md` ➡️ `02-first-principles.md` ➡️ `04-backend-stack.md` ➡️ `06-database-design.md`
