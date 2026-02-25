[🇰🇷 한국어 문서](README_KR.md)
[![BCC CI](https://github.com/yuuuuuh14/face/actions/workflows/bcc-ci.yml/badge.svg)](https://github.com/yuuuuuh14/face/actions/workflows/bcc-ci.yml)

# 👁️ BIOMETRIC_CONTROL_CENTER (BCC)

**Sci-Fi HUD-based Local Real-time Face Recognition System v3.5 Stable**

BIOMETRIC_CONTROL_CENTER (hereinafter BCC) is an **offline/local-only biometric dashboard** built by converging the latest machine learning models and modern web technologies.
It provides a beautiful UI/UX with a cyberpunk mood and supports both native and containerized (Docker) execution.

---

## ✨ Features
- 🎯 **High-Performance Face Recognition**: 512-dimensional feature vector extraction and cosine similarity matching based on InsightFace (`antelopev2`).
- 🛡️ **Anti-Spoofing (Liveness Detection)**: Simple and powerful forgery (photo/screen) defense logic using edge detection (Laplacian Variance).
- 📜 **Integrated Access Log Preservation (DB Log Dashboard)**: Automatically and permanently records face detection and spoofing passage status with timestamps in an SQLiteDB.
- 🐳 **Docker Support**: Full containerization via `docker-compose` for easy deployment and environment consistency.
- ⚙️ **CI/CD Pipeline**: Automated testing (GitHub Actions) for both Python (pytest) and Angular (Vitest) ensuring code quality.
- 🖥️ **Sci-Fi HUD Interface**: Cybernetic glow effects and Korean typography implemented with Angular Material and SCSS.
- ⚡ **Bi-directional Real-time Communication**: Delay-free overlay by combining MJPEG streaming and SSE (Server-Sent Events).

---

## 🛠️ Tech Stack

### Backend (Python 3.11+)
- **Framework**: Flask (REST API + SSE)
- **AI / Computer Vision**: OpenCV, InsightFace (ArcFace), ONNXRuntime
- **Storage**: Ultra-lightweight SQLite Database (`data/faces.db`)

### Frontend (Node.js 18+)
- **Framework**: Angular v15+ (Standalone Components based)
- **Styling**: Angular Material + Custom SCSS (Sci-Fi Theme)

---

## 🚀 Quick Start

BCC provides an **interactive startup script**. When you run it, you can choose between **Docker** and **Native** execution.

### 🍏 macOS / 🐧 Linux Environments
```bash
./run.sh
# Prompt: "🐳 Do you want to run with Docker? (y/N)"
```

### 🪟 Windows Environments
```cmd
run.bat
:: Prompt: "🐳 Do you want to run with Docker? (y/N)"
```

> **Verifying Success:**
> When the browser opens, navigate to `http://localhost:4200` and allow camera permissions.
> The backend data stream and **Automated API Documentation (Swagger)** are available at `http://localhost:8001/`. (Uses `faces.db` or `test_faces.db` based on the environment.)

---

## 📚 Documentation Archive
If you want to understand the BCC project deeply, please read the documents below in order.

- 🗺️ **[Project Planning and Architecture (PROJECT_PLAN_EN.md)](PROJECT_PLAN_EN.md)** - Architecture and progress by phase
- 🎯 **[Development Milestones (MILESTONES_EN.md)](MILESTONES_EN.md)** - Core development history and issue tracking
- 📖 **[Learning Workbook (docs/WORKBOOK_EN.md)](docs/WORKBOOK_EN.md)** - A comprehensive guidebook explaining the system's foundational principles and technical details

---
**License**: LGPL v2.1 
**Status**: Active / Supported
