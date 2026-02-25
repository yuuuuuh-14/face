[🇰🇷 한국어 문서](04-backend-stack.md)

# [04] In-depth Backend Anatomy: Threading and Model Engine

Why did we choose Python (Flask) as the main server?
This is because the vast majority of machine learning/AI ecosystem components (InsightFace, OpenCV, PyTorch, etc.) on Earth are implemented in Python, concentrating the ecosystem there.

## 1. Dilemma: GIL (Global Interpreter Lock) and Threading
If the thread where the web server (Flask) receives requests and the thread where InsightFace processes images are the same, the server will freeze. If model analysis takes 0.1 seconds, the frame rate would plummet to a mere 10 FPS.

Countermeasure:
1. **Main Camera Thread**: OpenCV focuses purely on fetching images and encoding them to JPEG. (Defense of at least 30 FPS with latency under 0.01 seconds)
2. **AI Analysis Worker Thread**: Copies the most recent photo and then analyzes it slowly. It is completely separated from the main video stream, preventing the video from stuttering.

## 2. Matching Algorithm: Cosine Similarity
The AI engine (ArcFace) converts a specific person's face into a 1D array (Vector) of 512 decimal points.
How should we determine if a new face vector A and a stored original vector B belong to the same person?

Instead of simple number subtraction (Euclidean distance), finding the **angle difference between vectors** (Cosine Similarity) is the most powerful technique. (It is very robust against wearing glasses, lighting changes, etc.)
- Logic Chain: `A · B / (||A|| * ||B||)`
- BCC Project's standard `Threshold`: If the similarity is above approximately **0.4**, it is considered the same person, triggering the green light (IDENTIFIED) and the name on the HUD. If below, it falls into the UNKNOWN (dangerous target) status.

All these mathematical formulas are calculated inside `model_manager.py`.
