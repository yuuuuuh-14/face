import cv2
import time
import logging
import threading

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CameraHandler:
    """Controls the camera device and captures frames using a background thread for non-blocking access."""
    def __init__(self, device_id=0):
        self.device_id = device_id
        self.cap = None
        self.frame = None
        self.ret = False
        self.running = True
        self.lock = threading.Lock()
        self.fail_count = 0
        
        self._open_camera()
        
        # Start background capture thread
        self.thread = threading.Thread(target=self._capture_loop, daemon=True)
        self.thread.start()
        
        self.prev_time = 0
        self.fps = 0

    def _open_camera(self):
        """Attempts to open the camera with various backends."""
        if self.cap is not None:
            self.cap.release()
            
        # Try DSHOW first (good for Windows webcams)
        self.cap = cv2.VideoCapture(self.device_id, cv2.CAP_DSHOW)
        if not self.cap.isOpened():
            logger.info(f"DSHOW failed for camera {self.device_id}, trying MSMF/Default")
            self.cap = cv2.VideoCapture(self.device_id, cv2.CAP_MSMF)
            
        if not self.cap.isOpened():
            logger.info(f"MSMF failed for camera {self.device_id}, trying default index")
            self.cap = cv2.VideoCapture(self.device_id)

        if not self.cap.isOpened():
            logger.error(f"All backends failed for camera {self.device_id}")
            # We don't raise here to allow the thread to potentially recover or the app to stay alive
            return False
            
        logger.info(f"Camera {self.device_id} opened successfully")
        return True

    def _capture_loop(self):
        """Background thread to continuously update the frame with auto-recovery."""
        while self.running:
            if self.cap is None or not self.cap.isOpened():
                self._open_camera()
                time.sleep(1)
                continue

            ret, frame = self.cap.read()
            if not ret:
                self.fail_count += 1
                if self.fail_count > 5:
                    logger.warning("Camera grab failed repeatedly, attempting reset")
                    self._open_camera()
                    self.fail_count = 0
                    time.sleep(1.0)
                else:
                    time.sleep(0.1)
                continue
                
            self.fail_count = 0
            with self.lock:
                self.ret = ret
                self.frame = frame
            time.sleep(0.01)

    def get_frame(self):
        """Returns the latest captured frame from the background thread."""
        with self.lock:
            if not self.ret or self.frame is None:
                return False, None
            return True, self.frame.copy()

    def calculate_fps(self):
        """Calculates and returns real-time FPS."""
        current_time = time.time()
        time_diff = current_time - self.prev_time
        self.fps = 1 / time_diff if time_diff > 0 else 0
        self.prev_time = current_time
        return self.fps

    def release(self):
        """Stops the loop and releases resources."""
        self.running = False
        if hasattr(self, 'thread') and self.thread.is_alive():
            self.thread.join(timeout=1.0)
        if self.cap and self.cap.isOpened():
            self.cap.release()
        logger.info(f"Camera {self.device_id} released")
