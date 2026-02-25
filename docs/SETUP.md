[🌐 EN VERSION](SETUP_EN.md)

# ⚙️ 시스템 설정 및 기동 가이드 (System Setup)

BIOMETRIC_CONTROL_CENTER(BCC)를 로컬 환경에서 구동하기 위한 공식 메뉴얼입니다.
BCC는 무거운 가상화 도구(Docker)를 완전히 배제하고 네이티브 OS 자원을 최대로 활용하도록 설계되었습니다.

---

## 💻 시스템 요구 사항 (Prerequisites)

- **OS**: Windows 10/11, macOS (M1/M2 지원 권장), 또는 Linux
- **Camera**: USB 웹캠 또는 내장 카메라 (노트북)
- **Backend**: Python 3.9 이상
- **Frontend**: Node.js 18.x (또는 20.x LTS) 및 Yarn 패키지 매니저
- **Git** & **VSCode** (선택 사항이지만 강력 권장)

---

## 🧠 시스템 1: AI 백엔드 커맨드 노드 기동

백엔드 파이프라인(Flask 서버 및 InsightFace 엔진)을 부트스트랩합니다.

1. **저장소 클론 및 루트 이동**
   ```bash
   git clone [레포지토리 주소] face_recognition_bcc
   cd face_recognition_bcc
   ```

2. **격리된 파이썬 생태계(venv) 구축**
   ```bash
   python -m venv venv
   ```
   > ⚠️ `venv` 폴더가 코어 로직과 섞이지 않도록 주의하십시오.

3. **가상 환경 활성화**
   ```bash
   # Windows PowerShell
   .\venv\Scripts\activate

   # macOS / Linux (BASH/ZSH)
   source venv/bin/activate
   ```
   > 터미널 프롬프트 앞에 `(venv)` 헤더가 표시되어야 합니다.

4. **의존 패키지 인스톨 및 서버 런칭**
   ```bash
   cd backend
   pip install -r ../requirements.txt
   python app.py
   ```
   > 정상 기동 시 터미널에 `Running on http://localhost:8001` 메세지가 뜹니다.

---

## 👁️ 시스템 2: 프론트엔드 HUD 인터페이스 기동

Visual 레이어(Angular) 서버를 부트스트랩합니다.
**반드시 새로운 터미널 탭/창을 열어서 실행**해야 합니다. (백엔드를 종료하지 마세요!)

1. **UI 패키지 인스톨**
   ```bash
   cd frontend
   yarn install
   ```

2. **개발 모드 징발 (Angular Live Server)**
   ```bash
   yarn start
   ```
   > 정상 기동 시 `http://localhost:4200` 에서 HUD 터미널을 열람할 수 있습니다.

---

## 🚀 기동 테스트 및 권한 확인

모든 시스템이 구동되었다면 브라우저를 열고 `http://localhost:4200` 에 접속합니다.
1. 브라우저에서 묻는 **'카메라 / 비디오 사용 권한'** 을 반드시 `허용(Allow)` 해야 합니다.
2. 좌측 상단 카메라 디스플레이 뷰에 자신의 얼굴이 나오고 노란색 타겟팅 박스와 스캔 라인이 정상 동작하는지 확인합니다.

---

### 빠른 접속 문제 해결 (Troubleshooting)
- **Q: 화면이 뜨지 않거나 API 연결 거부가 발생합니다.**
  A: 백엔드 터미널(8001 포트)이 켜져 있고 `app.py` 프로세스가 실행 중인지 확인하세요.
- **Q: InsightFace 로딩 중 다운로드가 멈춥니다.**
  A: 처음 실행 시 ArcFace 모델 파일(약 200~300MB)을 `~/.insightface` 경로로 다운로드합니다. 이 과정에서 네트워크 환경에 따라 수 분이 소요될 수 있습니다.

> 추가적인 내용은 `docs/WORKBOOK.md` 내 트러블슈팅 세션을 참고하십시오.
