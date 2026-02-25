import cv2
import numpy as np
import logging
import os
from insightface.app import FaceAnalysis

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ModelManager:
    """Handles face detection and recognition with explicit caching and fallback."""
    def __init__(self, model_name='antelopev2', model_root=None):
        self.is_mock = False
        self.app = None
        
        try:
            # Ensure model root exists
            if model_root:
                os.makedirs(model_root, exist_ok=True)
                
            # Initialize InsightFace with explicit root
            self.app = FaceAnalysis(
                name=model_name, 
                root=model_root,
                providers=['CPUExecutionProvider']
            )
            self.app.prepare(ctx_id=0, det_size=(640, 640))
            logger.info(f"InsightFace engine '{model_name}' initialized at {model_root}")
        except Exception as e:
            self.is_mock = True
            logger.warning(f"AI Model load failed (switching to MOCK mode): {e}")

    def get_analysis(self, frame):
        """Detects faces. Returns empty list if in MOCK mode."""
        if self.is_mock or frame is None:
            return []
            
        try:
            return self.app.get(frame)
        except Exception as e:
            logger.error(f"Detection error: {e}")
            return []

    def draw_faces(self, frame, faces):
        """Draws results. Skips if in MOCK mode."""
        if self.is_mock:
            return frame
            
        for face in faces:
            bbox = face.bbox.astype(int)
            is_unknown = getattr(face, 'name', 'UNKNOWN') == 'UNKNOWN'
            color = (0, 0, 255) if is_unknown else (0, 255, 0)
            cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
            name = getattr(face, 'name', "UNKNOWN")
            cv2.putText(frame, name, (bbox[0], bbox[1] - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        return frame

    @staticmethod
    def compute_similarity(feat1, feat2):
        if feat1.shape != feat2.shape:
            return 0.0
        norm1 = np.linalg.norm(feat1)
        norm2 = np.linalg.norm(feat2)
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return np.dot(feat1, feat2) / (norm1 * norm2)

    def analyze_liveness(self, frame, bbox, threshold=50.0):
        """Liveness heuristic. Returns 'REAL' in MOCK mode to allow testing."""
        if self.is_mock:
            return "REAL"
            
        try:
            x1, y1, x2, y2 = [int(v) for v in bbox]
            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(frame.shape[1], x2), min(frame.shape[0], y2)
            face_roi = frame[y1:y2, x1:x2]
            if face_roi.size == 0: return "UNKNOWN"
            gray = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
            fm = cv2.Laplacian(gray, cv2.CV_64F).var()
            return "REAL" if fm > threshold else "SPOOF"
        except Exception:
            return "UNKNOWN"

    def find_match(self, face_embedding, registered_faces, threshold=0.4):
        if self.is_mock:
            return ("UNKNOWN", 0.0)
            
        best_name, best_score = "UNKNOWN", 0.0
        for reg_face in registered_faces:
            sim = self.compute_similarity(face_embedding, np.array(reg_face['embedding']))
            if sim > best_score:
                best_score, best_name = sim, reg_face['name']
        return (best_name, best_score) if best_score >= threshold else ("UNKNOWN", best_score)
