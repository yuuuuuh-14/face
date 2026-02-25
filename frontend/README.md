# 👁️ BCC: Frontend HUD Module (Angular workspace)

이 디렉토리는 **BIOMETRIC_CONTROL_CENTER (BCC)** 의 시각적 대시보드(Sci-Fi HUD) 렌더링을 담당하는 Angular 기반 프론트엔드 프로젝트입니다.

## 1. 개요
백엔드(Flask)에서 실시간으로 쏘아주는 MJPEG 비디오 스트림과 SSE 이벤트 데이터를 병합하여, 사용자의 브라우저 화면에 오버레이 애니메이션(바운딩 박스, 스피드 메트릭스 등)을 부드럽게を描画(드로잉) 합니다.

## 2. 기술 스택
- **Framework**: Angular v15+ (Standalone Components 적용)
- **UI Components**: Angular Material (Dialog, Tables, Buttons)
- **Styling**: SCSS (Custom Neon Glow & Scanlines Effects)
- **Async Handling**: RxJS (SSE Observer, Interval Polling)

## 3. 로컬 개발 환경 런칭 (Development server)

이 프로젝트를 실행하기 전에 **반드시 백엔드 모듈이 8001 포트에서 런칭되어 있어야** 카메라 화면과 데이터가 정상적으로 들어옵니다.

```bash
# 의존성 패키지 설치
yarn install

# 개발용 라이브 서버 런칭
yarn start
```

서버가 구동되면 브라우저를 열고 `http://localhost:4200/` 에 접속하십시오.
코드를 수정할 때마다 Angular Live Development Server 가 자동으로 변경 사항을 감지하여 브라우저를 리로드(Hot Reload) 합니다.

## 4. 빌드 (Build)
만약 이 Angular 앱을 프로덕션(Nginx 등)에 배포할 목적이라면 아래 명령어로 정적 에셋 스태틱 빌드를 수행하십시오.

```bash
yarn build
```
빌드 산출물은 `dist/` 폴더 내부에 생성됩니다.

## 5. 핵심 디렉토리 및 소스 위치
- `src/app/` : 비즈니스 로직과 HUD 컴포넌트(`*.component.ts`), 그리고 각각의 뷰 템플릿(`*.html`)이 위치.
- `src/styles.scss` : 프로젝트 전역에 적용되는 공통 사이버펑크 테마 및 애니메이션 키프레임 정의.
- `src/assets/` : 필요한 경우 정적 이미지 스크린 로고 등 포함.

> 📚 전체 시스템 파이프라인과 프론트엔드의 작동 원리는 프로젝트 최상단 루트의 `docs/WORKBOOK.md` 내부의 `[05-frontend-stack.md]` 챕터에 매우 상세하게 설명되어 있습니다. 반드시 해당 워크북을 참고하세요.
