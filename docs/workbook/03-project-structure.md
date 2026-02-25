[🌐 EN VERSION](03-project-structure_EN.md)

# [03] 시스템 구조 (Architecture) 및 통신 파이프라인

BCC 프로젝트는 크게 두 가지 컨테이너(Flask, Angular) 사이의 통신망으로 이루어져 있습니다. 이 둘은 같은 로컬 머신 (ex: 노트북) 안에 존재합니다.

## 시스템 모식도

```text
[ 카메라 디바이스 ]  -------- (cv2.VideoCapture) -------->  [ Flask (AI & Backend) ]  <----> [ SQLite DB ]
                                                               |   |   |
  +------------------------------------------------------------+   |   |
  | MJPEG Video Stream (Port 8001 /api/video_feed)                 |   |
  |                 +----------------------------------------------+   |
  |                 | SSE Telemetry Data (Port 8001 /api/stream)       |
  |                 |              +-----------------------------------+
  V                 V              | REST API Commands (Port 8001 /api/xyz)
[ Angular (Frontend HUD) ] <-------+
```

## 핵심 모듈 분석

### 1. Flask 서버 (Port 8001)
데이터를 만들어내는 원천(Source) 이자 제어 타워입니다.
- `app.py`: 웹훅 라우팅 및 런처 로직.
- `camera.py`: 백그라운드에 숨겨진 무한 루프 스레드. `cv2.VideoCapture(0)` 로 화면을 빨아들여 버퍼 큐에 적재합니다.
- `model_manager.py`: InsightFace 모델 인스턴스의 뇌(Brain) 역할을 합니다. 사진 프레임을 주면 512차원의 벡터, 바운딩 박스, 성별/데이터를 뱉어냅니다.

### 2. 단방향, 그러나 초고속: SSE (Server-Sent Events)
Angular는 백엔드의 지표를 계속 서버에 물어볼 필요가 없습니다. (Polling 낭비 방지).
Flask 내의 SSE 엔드포인트에 소켓 빨대를 하나 꽂아두면, 백엔드가 프레임 분석을 마칠 때마다 `{"faces": [{"bbox": [], "name": "...", "age": 28}], "fps": 29}` 와 같은 JSON 데이터를 끊임없이 프론트엔드로 밀어내줍니다(Push).

### 3. Angular 프론트엔드 (Port 4200)
수신기의 역할입니다.
- `<img class="video-layer">`: 맨 밑바닥에 Flask 가 쏴주는 무한 이미지 비디오를 깔아놓습니다.
- `<svg class="overlay-layer">`: 그 위에 투명 플라스틱 판(SVG 캔버스)을 하나 덮습니다.
- 컴포넌트 로직은 SSE로 날아오는 JSON `bbox`의 좌표점대로 SVG 레이어에 마커를 그렸다 지웠다 반복합니다.
- 이게 사람이 보기엔 엄청난 속도로 박스가 따라다니는 것처럼 보이게 되는 것입니다.
