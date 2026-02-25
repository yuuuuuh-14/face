import os
import cv2
import logging
import base64
import time
import threading
import json
from flask import Flask, render_template, Response, request, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource, fields, Namespace

from camera.camera_handler import CameraHandler
from models.model_manager import ModelManager
from database.storage_manager import storage

from config import get_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration based on environment
conf = get_config()

app = Flask(__name__)
app.config.from_object(conf)
CORS(app, resources={r"/*": {"origins": conf.CORS_ORIGINS}})

# API initialization
api = Api(app, version='1.0', title='BCC Biometric API',
          description='Automated Swagger UI for Biometric Control Center',
          doc='/') # Swagger UI at root

# Namespaces
face_ns = api.namespace('face', description='Face Management Operations')
stream_ns = api.namespace('stream', description='Real-time Data Streaming')
logs_ns = api.namespace('logs', description='Access History Logs')
system_ns = api.namespace('system', description='System Diagnostics')

# Models for Swagger documentation
register_model = api.model('RegisterFace', {
    'name': fields.String(required=True, description='Name of the person to register')
})

face_info_model = api.model('FaceInfo', {
    'names': fields.List(fields.String, description='List of registered names')
})

log_model = api.model('Log', {
    'id': fields.Integer,
    'name': fields.String,
    'timestamp': fields.String,
    'liveness': fields.String
})

health_model = api.model('Health', {
    'status': fields.String,
    'camera_connected': fields.Boolean
})

_camera = None
_model_manager = None
model_lock = threading.Lock() # Prevent concurrent model access

def get_camera():
    global _camera
    if _camera is None:
        if os.getenv('BCC_ENV') == 'testing':
            logger.info("Skipping camera initialization in testing environment")
            return None
        _camera = CameraHandler(0)
    return _camera

def get_model_manager():
    global _model_manager
    if _model_manager is None:
        if os.getenv('BCC_ENV') == 'testing':
            logger.info("Skipping model manager initialization in testing environment")
            return None
        _model_manager = ModelManager(
            model_name=conf.MODEL_NAME,
            model_root=conf.MODEL_ROOT
        )
    return _model_manager

def generate_frames():
    """MJPEG stream generator with real-time face analysis."""
    cam = get_camera()
    model = get_model_manager()
    while True:
        if not cam:
            time.sleep(1)
            continue
            
        success, frame = cam.get_frame()
        if not success:
            time.sleep(0.1)
            continue
        
        registered_faces = storage.get_all_faces()
        
        with model_lock:
            if model:
                faces = model.get_analysis(frame)
                for face in faces:
                    name, score = model.find_match(face.embedding, registered_faces)
                    face.name = name
                frame = model.draw_faces(frame, faces)
        
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
            
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
        time.sleep(0.01)

# Throttling state
log_throttle_cache = {}
LOG_THROTTLE_SECONDS = 5.0

def generate_analysis_events():
    """Server-Sent Events generator for real-time analysis data."""
    logger.info("SSE analysis stream started")
    cam = get_camera()
    model = get_model_manager()
    while True:
        if not cam:
            time.sleep(1)
            continue
            
        success, frame = cam.get_frame()
        if success:
            registered_faces = storage.get_all_faces()
            with model_lock:
                if model:
                    faces = model.get_analysis(frame)
                    results = []
                    
                    current_time = time.time()
                    
                    for face in faces:
                        name, score = model.find_match(face.embedding, registered_faces)
                        bbox = face.bbox.astype(int).tolist()
                        
                        raw_gender = getattr(face, 'gender', -1)
                        gender_str = "MALE" if raw_gender == 1 else "FEMALE" if raw_gender == 0 else "UNKNOWN"
                        age_val = int(getattr(face, 'age', 0))
                        
                        liveness_str = model.analyze_liveness(frame, bbox)
                        
                        # Throttling 및 DB 접근 로그 기록
                        last_logged = log_throttle_cache.get(name, 0.0)
                        if current_time - last_logged > LOG_THROTTLE_SECONDS:
                            storage.log_access(name, liveness_str)
                            log_throttle_cache[name] = current_time
                        
                        results.append({
                            "bbox": bbox,
                            "name": name,
                            "score": float(face.det_score),
                            "match_score": float(score),
                            "gender": gender_str,
                            "age": age_val,
                            "liveness": liveness_str
                        })
            
            json_data = json.dumps({"faces": results})
            yield f"data: {json_data}\n\n"
        
        time.sleep(0.12)

@stream_ns.route("/video")
class VideoFeed(Resource):
    @stream_ns.doc('video_stream')
    def get(self):
        """MJPEG Video Streaming Endpoint"""
        return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@stream_ns.route("/events")
class AnalysisEvents(Resource):
    @stream_ns.doc('analysis_sse')
    def get(self):
        """SSE Analysis Data Endpoint"""
        return Response(generate_analysis_events(), mimetype='text/event-stream')

@face_ns.route("/register")
class RegisterFace(Resource):
    @face_ns.expect(register_model)
    def post(self):
        """Register the face currently visible in the camera"""
        data = request.json
        name = data.get('name')
        
        if not name:
            return {"success": False, "message": "Name is required"}, 400
            
        cam = get_camera()
        model = get_model_manager()
        
        if not cam:
            return {"success": False, "message": "Camera not available"}, 500
            
        success, frame = cam.get_frame()
        if not success:
            return {"success": False, "message": "Camera not ready"}, 500
            
        with model_lock:
            if not model:
                return {"success": False, "message": "AI Model not loaded"}, 500
                
            faces = model.get_analysis(frame)
            if not faces:
                return {"success": False, "message": "No face detected. Please look at the camera."}, 400
                
            face = max(faces, key=lambda f: (f.bbox[2]-f.bbox[0]) * (f.bbox[3]-f.bbox[1]))
            storage.save_face(name, face.normed_embedding.tolist())
            
        return {"success": True, "message": f"Face registered for {name}"}

@face_ns.route("/")
class FaceList(Resource):
    @face_ns.marshal_with(face_info_model)
    def get(self):
        """List all registered face names"""
        faces = storage.get_all_faces()
        return {"success": True, "names": [f['name'] for f in faces]}

@face_ns.route("/<string:name>")
@face_ns.param('name', 'The name of the subject to delete')
class FaceDetail(Resource):
    def delete(self, name):
        """Delete a registered face"""
        if storage.delete_face(name):
            return {"success": True, "message": f"Subject '{name}' removed."}
        else:
            return {"success": False, "message": f"Subject '{name}' not found."}, 404

@logs_ns.route("/")
class LogList(Resource):
    @logs_ns.doc(params={'limit': 'Number of logs to return (default 50)'})
    def get(self):
        """Fetch recent access history logs"""
        limit = request.args.get('limit', default=50, type=int)
        logs = storage.get_recent_logs(limit=limit)
        return {"success": True, "logs": logs}

@system_ns.route("/health")
class HealthCheck(Resource):
    @system_ns.marshal_with(health_model)
    def get(self):
        """System health and camera status"""
        cam = get_camera()
        return {
            "status": "ok", 
            "camera_connected": cam.cap.isOpened() if cam and cam.cap else False
        }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8001))
    app.run(host="0.0.0.0", port=port, debug=conf.DEBUG, threaded=True)
