[🇰🇷 한국어 문서](12-quick-reference.md)

# [12] Tactical Cheat Sheet (Quick Status Reference)

This is a summary encyclopedia of commands and APIs necessary for debugging and maintaining the BCC project.
There's no need to memorize them; just look into them frequently.

## Terminal Commands

```bash
# === Powerful Wipe Command: Completely Nuke Python Virtual Environment ===
# (A last resort when dependencies are hopelessly twisted. Reinstall afterwards.)
rm -rf backend/venv

# === Completely Nuke Angular Dependencies ===
rm -rf frontend/node_modules
rm -rf frontend/dist

# === Reinstall Python Requirements ===
cd backend
source venv/bin/activate
pip install -r ../requirements.txt
```

---

## B.C.C Core API Endpoint Blueprint (Backend 8001)

All data flows out pivoting around the Flask server (Port 8001). The frontend code is mapped to this specification.

### 🌐 [Communication Channel] `GET /api/stream`
- **Purpose**: Infinite delayed event (JSON) dispatcher (SSE)
- **Payload Structure**: `{"faces": [ {"bbox": [...], "name": "Admin", "age": 31} ], "fps": 29 }`
- **Method**: Subscribing to the socket with Angular's built-in `EventSource`

### 🎥 [Streaming Channel] `GET /api/video_feed`
- **Purpose**: Infinite loop streaming of camera images (MJPEG)
- **Method**: Hardcoded into the `src` address of the browser's `img` tag

### 🛡️ [Command Control] `POST /api/register`
- **Purpose**: Order to add local registration of a person vector
- **Body**: `{ "name": "Name of Agent to Register" }`
- **Note**: The server instantly maps the fleeting vector currently floating in the thread memory and re-transmits the JSON file.

### 🛡️ [Command Control] `GET /api/faces`
- **Purpose**: Fetch the registered directory list (JSON Array) and print it on the screen

### 🛡️ [Command Control] `DELETE /api/delete_face`
- **Purpose**: Erase an agent of a specific name
- **Body**: `{ "name": "Name of Agent to Delete" }`
