[🇰🇷 한국어 문서](03-project-structure.md)

# [03] System Architecture and Communication Pipeline

The BCC project mainly consists of a communication network between two containers (Flask, Angular). Both exist within the same local machine (e.g., a laptop).

## System Schematic Diagram

```text
[ Camera Device ]  -------- (cv2.VideoCapture) -------->  [ Flask (AI & Backend) ]  <----> [ SQLite DB ]
                                                               |   |   |
  +------------------------------------------------------------+   |   |
  | MJPEG Video Stream (Port 8001 /api/video_feed)                 |   |
  |                 +----------------------------------------------+   |
  |                 | SSE Telemetry Data (Port 8001 /analysis_events)  |
  |                 |              +-----------------------------------+
  V                 V              | REST API Commands (Port 8001 /register, /faces)
[ Angular (Frontend HUD) ] <-------+
```

## Core Module Analysis

### 1. Flask Server (Port 8001)
The source that produces data and the control tower.
- `app.py`: Webhook routing and launcher logic.
- `camera.py`: The infinite loop thread hidden in the background. It sucks in the screen with `cv2.VideoCapture(0)` and loads it into the buffer queue.
- `model_manager.py`: Acts as the brain of the InsightFace model instance. Given a photo frame, it spits out a 512-dimensional vector, bounding box, gender/age data, and Liveness score.

### 2. Unidirectional, yet Ultra-fast: SSE (Server-Sent Events)
Angular doesn't need to keep asking the server for backend indicators. (Prevents polling waste).
If you plug a socket straw into the SSE endpoint in Flask, every time the backend finishes framing analysis, it endlessly pushes JSON data like `{"faces": [{"bbox": [], "name": "...", "age": 28}], "fps": 29}` to the frontend.

### 3. Angular Frontend (Port 4200)
The role of the receiver.
- `<img class="video-layer">`: At the very bottom, it lays out the infinite image video shot by Flask.
- `<svg class="overlay-layer">`: On top of that, it covers a transparent plastic plate (SVG canvas).
- Component logic repeatedly draws and erases markers on the SVG layer according to the coordinates of the JSON `bbox` flying via SSE.
- To a human eye, this makes it look as if the box is following the person at incredible speed.
