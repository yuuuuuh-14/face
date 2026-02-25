[🇰🇷 한국어 문서](PROJECT_PLAN.md)

# 🗺️ BIOMETRIC_CONTROL_CENTER Planning and Architecture

This document guides the system design philosophy, structure, and development phases of **BIOMETRIC_CONTROL_CENTER (v3.5 Stable)**.

---

## 1. Project Vision
The goal is to implement a **'Futuristic Security Control Center (Sci-Fi HUD)'**, akin to those seen in movies or games, into reality.
- **Offline-First**: Operates solely in a local environment without external internet or heavy cloud infrastructure connections.
- **Lightweight and Intuitive**: Uses an intuitive `JSON` based storage repository instead of complex RDBMS.
- **Aesthetic Fulfillment**: Provides a beautiful and grand dashboard UI experience, escaping clunky analysis screens.

---

## 2. System Architecture

The system is divided into two layers with clear divisions of roles.

### 🧠 Backend (AI & Data Pipeline)
Controls the camera hardware and performs heavy AI computations.
1. **CV Pipeline (OpenCV)**: Captures a distortion-free 30fps video stream (MJPEG) from the main thread.
2. **AI Worker (InsightFace)**: Asynchronously performs face detection, feature vector extraction, biometric information (gender/age) analysis, and anti-spoofing (Liveness) determination in a background thread.
3. **Match Engine**: Compares the vector of the detected face in real-time with the `SQLite` data (Euclidean Distance/Cosine Similarity) of already registered individuals.
4. **Access DB Logger**: Automatically saves the face detection event details (Timestamp, Liveness, etc.) that passed through the throttling logic into SQLite (`access_history`).
5. **Event Broadcaster (Flask SSE & REST API)**: Pushes/provides the computed AI metadata and DB logs to the frontend without delay.

### 👁️ Frontend (Sci-Fi HUD)
Visually and gorgeously renders the data pushed from the backend.
1. **Video Layer**: Plays the backend's `/api/video_feed` (MJPEG) seamlessly in the background.
2. **Overlay Renderer (Angular)**: Smoothly draws scanning animations and bounding boxes in accordance with coordinate data received via the SSE socket, at a level equivalent to a 120Hz refresh rate.
3. **Interactive Dashboard (Angular Material)**: Delivers commands such as person registration, target deletion, and system log verification to the backend via `/api/xyz` REST APIs.

---

## 3. Development Phases

### 🟢 Phase 1: Core Engine Bootstrap (Completed)
- Camera hardware integration and video flow server (MJPEG) construction.
- ArcFace-based precision face detection module integration.
- Generation of the basic Flask server skeleton.

### 🟢 Phase 2: Data Persistence and Identification (Completed)
- Establishment of a local feature vector `SQLite DB` automatic management system rather than memory-based.
- Design of enrolling logic based on face information (photo + name).
- Completion of the Unregistered (UNKNOWN) and Identified (IDENTIFIED) target classification process.

### 🟢 Phase 3: Experience Enhancement: Sci-Fi HUD (Completed)
- 100% reorganization of front-end technologies from legacy vanilla/templates to an **Angular** structure.
- Application of SCSS effects (Glow, Scanlines) for a Cybernetic mood.
- Korean user-friendly experience (UX) improvement and introduction of Korean web fonts.

### 🟢 Phase 4: Biometric Intelligence Expansion and Optimization (Completed)
- Equipping additional metadata extraction layers such as **Gender / Age estimation**.
- Mitigating bottleneck hurdles through threading and asynchronous processing structure refactoring.
- **Dockerization**: Built a one-click deployment environment via `docker-compose`.
- **CI/CD Pipeline**: Implementation of automated build and testing via GitHub Actions (Pytest, Vitest).
- Complete renewal of documentation and enhancement of interactive startup scripts (`run.sh`, `run.bat`).

---

## 4. Final Success Criteria Evaluation
- [x] **Real-time Guarantee**: Stably maintain video stream frame rate (20~30fps).
- [x] **Accuracy Security**: Ensure high matching recognition rate based on the InsightFace model.
- [x] **Data Integrity**: Eliminate data loss or overwrite logic errors during local DB (JSON) I/O.
- [x] **Visual Wow Point**: Perfect implementation of the Sci-Fi theme differentiated from typical dashboards.
