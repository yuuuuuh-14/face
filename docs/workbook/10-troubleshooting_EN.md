[🇰🇷 한국어 문서](10-troubleshooting.md)

# [10] Tactical Monitoring: Fault and Incident Troubleshooting

These are countermeasures for system errors and shutdown symptoms you might encounter during BCC system operation.

## 🚨 Issue 1: `cv2.error` or Black Screen Freeze
**(Symptom)** Red errors spew in the terminal when booting Flask, or the frontend camera screen freezes in black.
**(Diagnosis)** Another program (Zoom, OBS, Web Browser) is monopolizing the system camera resources (Lock state). Or the hardware `/dev/video0` index is not 0.
**(Solution)**
- Completely turn off all video conferencing programs.
- In a Mac environment, check if the **'Camera Access Permission (Privacy -> Camera)'** is unchecked in the Terminal app or Editor app.
- Try adjusting the index of the external webcam by changing the number inside the parentheses of `cv2.VideoCapture(0)` in the `camera.py` lines to 1, 2, etc.

---

## 🚨 Issue 2: "InsightFace Module Download Error"
**(Symptom)** Freezes when turning on the backend for the first time, then throws a `ConnectionError` or `Timeout` type error.
**(Diagnosis)** The ArcFace model is stored externally (mostly Google Drive or overseas servers) as an `.onnx` binary. When downloading this locally (cache folder) for the first time, it gets blocked by a firewall or network policy.
**(Solution)**
- Try blowing away the entire `/models/` directory inside the local user folder `~/.insightface/` and reboot.
- If it still doesn't work, manually find the `antelopev2` (compressed pack) file in `.onnx` format from InsightFace's official GitHub release forum and perform an offline extract copy to `~/.insightface/`.

---

## 🚨 Issue 3: Angular SSE Frame Bounding Box Jitters or Causes Massive Lag
**(Symptom)** The camera screen is smooth, but the green square box fails to stick to the frame in time, and an afterimage chases belatedly.
**(Diagnosis)** `ChangeDetectionStrategy` is forced to OnPush, or the Python thread is overloaded (laptop CPU throttling).
**(Solution)**
- Minorly adjust the `time.sleep()` value, the defensive logic that skips frames allocated on the Python side.
- Carefully inspect the source code to ensure coordinate variables are being modified only inside the `ngZone` within the Angular code.
