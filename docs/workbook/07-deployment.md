[🌐 EN VERSION](07-deployment_EN.md)

# [07] 배포와 가상 환경의 멘탈 모델 (Mental Model for Python Env)

대기업 프로덕션이라면 당연히 Kubernetes나 Docker Swarm을 사용하겠지만, **BIOMETRIC_CONTROL_CENTER (BCC)**는 로컬 컴퓨터(노트북)에서 즉시 동작하는 것이 최우선 원칙입니다.

이 원칙을 지키면서 시스템을 오염시키지 않으려면 파이썬 생태계의 **"가상 환경 (Virtual Environment)"** 패러다임을 확고히 이해해야 합니다.

## 1. 글로벌 파이썬 지옥(Global Python Hell)
초보자들이 가장 흔히 저지르는 실수가 터미널에 무작정 `pip install opencv-python insightface flask` 를 타이핑하는 것입니다.
이렇게 되면 OS에 내장된 메인 Python 환경에 모든 패키지가 섞이게 되어, 내일 다른 프로젝트(Ex: Django 앱)를 실행할 때 버전 충돌이 발생해 전부 망가져 버립니다.

## 2. 결계 치기: `python -m venv venv`
Python 3 부터는 `venv` 라는 자체 모듈이 내장되어 있습니다. 루트 프로젝트 안의 `backend` 하위 디렉토리로 이동한 뒤 `python -m venv venv` 를 실행하십시오.

- 폴더 이름 자체인 `venv/` (Visual Studio Code나 PyCharm은 자동으로 이 폴더를 회피합니다)가 내부에 파이썬 인터프리터(`python.exe`)와 패키지 저장소(`site-packages`)를 완전히 새롭게 복제해냅니다.
- **Activate (활성화)**: `source venv/bin/activate` (Mac/Linux) 혹은 `.\venv\Scripts\activate` (Windows)를 치면 이 마법이 발동됩니다. 터미널 명령줄 제일 윗단에 괄호 쳐진 `(venv)` 가 등장하면, 이후 여러분이 치는 모든 `pip` 와 `python` 명령어는 OS를 벗어나 이 격리된 폴더 안에서 맴돌게 됩니다.

## 3. Git 오염 방어: `.gitignore`
가상환경 안에 수십 개의 패키지가 수 기가바이트(GB)씩 인스톨되어 있는데, 이걸 `git commit` 해버리면 끔찍한 비극이 초래됩니다.
루트의 `.gitignore` 파일을 보시면 `venv/` 가 최상단에 강력하게 차단되어 있는 이유입니다.
우리는 가상환경 결과물이 아니라 `requirements.txt` 라는 "설계도" 만 Git 저장소에 공유합니다.

> 팁: 프론트엔드의 `node_modules` 도 완전히 똑같은 이치로 Git 격리 조치가 적용됩니다. Angular와 Flask 개발의 기초는 버전 관리에서 제외시킬 대상을 명확히 하는 것에서 시작합니다.
