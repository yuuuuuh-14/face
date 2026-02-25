[🇰🇷 한국어 문서](02-first-principles.md)

# [02] First Principles: The Essence of Computer Vision and Face Processing

To understand the BCC project, it is necessary to grasp how the system processes video.

## 1. Frame Continuity (MJPEG Basics)
Typical video streaming protocols (H.264, WebRTC) are very complex. Codecs must be installed, and the protocol stack is deep.
However, the BCC project fundamentally pursues simplicity.
We chose a rudimentary and fast method (MJPEG - Motion JPEG) where continuous frames of the venue obtained from the camera are compressed into **JPEG images** and then shot to the frontend.

* The backend's `/api/video_feed` is a multipart HTTP responder that endlessly and infinitely calls `yield`.
* The frontend simply reads this address as `<img src="/api/video_feed">`, and the video plays.

## 2. Difference Between 'Detection' and 'Recognition'
These two words are easily conflated, but they are clearly different in AI pipelines.

- **Detection**: The process of simply finding "There is a face here" and identifying the Bounding Box location within a frame.
  - In this project, facial areas and eye/nose/mouth (landmark) locations are obtained at astonishing speeds via `insightface.app.FaceAnalysis`.
  - By adding a pipeline here, the target's **Age & Gender** are also initially inferred at this stage.

- **Recognition (= Matching)**: The process of guessing "Who on earth is this" detected target.
  - The AI model (ArcFace) converts the pixel information of the detected facial area into a 512-number Feature Vector (Embedding Array).
  - We find the identity by comparing this vector with our `SQLite` database (existing member vectors). 

As this process occurs repeatedly every frame or periodically in a background thread, the Sci-Fi HUD overlay indicators on the monitor change.
