[🇰🇷 한국어 문서](SETUP.md)

# ⚙️ System Setup and Boot Guide (System Setup)

This is the official manual for running the BIOMETRIC_CONTROL_CENTER (BCC) in a local environment.
BCC is designed to completely exclude heavy virtualization tools (Docker) and maximize the utilization of native OS resources.

---

## 💻 System Prerequisites

- **OS**: Windows 10/11, macOS (M1/M2 support recommended), or Linux
- **Camera**: USB Webcam or Built-in Camera (Laptop)
- **Backend**: Python 3.9 or higher
- **Frontend**: Node.js 18.x (or 20.x LTS) and Yarn package manager
- **Git** & **VSCode** (Optional but highly recommended)

---

## 🧠 System 1: Booting the AI Backend Command Node

Bootstraps the backend pipeline (Flask server and InsightFace engine).

1. **Clone Repository and Move to Root**
   ```bash
   git clone [Repository URL] face_recognition_bcc
   cd face_recognition_bcc
   ```

2. **Build an Isolated Python Ecosystem (venv)**
   ```bash
   python -m venv venv
   ```
   > ⚠️ Be careful not to mix the `venv` folder with the core logic.

3. **Activate Virtual Environment**
   ```bash
   # Windows PowerShell
   .\venv\Scripts\activate

   # macOS / Linux (BASH/ZSH)
   source venv/bin/activate
   ```
   > The `(venv)` header should be displayed in front of the terminal prompt.

4. **Install Dependency Packages and Launch Server**
   ```bash
   cd backend
   pip install -r ../requirements.txt
   python app.py
   ```
   > Upon successful boot, the message `Running on http://localhost:8001` will appear in the terminal.

---

## 👁️ System 2: Booting the Frontend HUD Interface

Bootstraps the Visual layer (Angular) server.
**You must open and run this in a new terminal tab/window.** (Do not close the backend!)

1. **Install UI Packages**
   ```bash
   cd frontend
   yarn install
   ```

2. **Requisition Development Mode (Angular Live Server)**
   ```bash
   yarn start
   ```
   > Upon successful boot, you can view the HUD terminal at `http://localhost:4200`.

---

## 🚀 Boot Test and Permission Verification

Once all systems are running, open your browser and navigate to `http://localhost:4200`.
1. You must `Allow` the **'Camera / Video use permission'** asked by the browser.
2. Check if your face appears on the top-left camera display view and if the yellow targeting box and scan lines are operating normally.

---

### Quick Troubleshooting
- **Q: The screen does not appear or an API connection refusal occurs.**
  A: Ensure the backend terminal (port 8001) is turned on and the `app.py` process is running.
- **Q: The download freezes while loading InsightFace.**
  A: During the first run, it downloads the ArcFace model file (approx. 200~300MB) to the `~/.insightface` path. This process may take several minutes depending on your network environment.

> For additional details, please refer to the troubleshooting session within `docs/workbook/10-troubleshooting_EN.md`.
