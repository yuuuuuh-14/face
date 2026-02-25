import sqlite3
import json
import os
import numpy as np
import logging

from config import get_config

logger = logging.getLogger(__name__)

class FaceDataStorage:
    """등록된 얼굴 정보를 SQLite 데이터베이스로 관리하는 클래스"""
    def __init__(self, storage_path=None):
        if storage_path is None:
            self.storage_path = get_config().DATABASE_PATH
        else:
            self.storage_path = storage_path
            
        # 데이터 디렉토리 생성
        if os.path.dirname(self.storage_path):
            os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        self._init_db()

    def _get_connection(self):
        """SQLite 데이터베이스 커넥션 반환"""
        # check_same_thread=False for multi-threading in Flask (e.g. SSE loops)
        return sqlite3.connect(self.storage_path, check_same_thread=False)

    def _init_db(self):
        """데이터베이스 테이블 초기화"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS faces (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE NOT NULL,
                        embedding TEXT NOT NULL
                    )
                ''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS access_history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        liveness TEXT NOT NULL
                    )
                ''')
                conn.commit()
        except Exception as e:
            logger.error(f"데이터베이스 초기화 중 오류 발생: {e}")

    def save_face(self, name, embedding):
        """새로운 인물 정보를 SQLite에 저장"""
        try:
            # NumPy 배열을 리스트로 변환 후 JSON 문자열로 직렬화
            emb_list = embedding.tolist() if isinstance(embedding, np.ndarray) else embedding
            emb_str = json.dumps(emb_list)
            
            with self._get_connection() as conn:
                cursor = conn.cursor()
                # 이미 존재하는 이름이면 덮어쓰기 (upsert)
                cursor.execute('''
                    INSERT INTO faces (name, embedding) 
                    VALUES (?, ?) 
                    ON CONFLICT(name) DO UPDATE SET embedding=excluded.embedding
                ''', (name, emb_str))
                conn.commit()
            logger.info(f"SQLite 파일에 데이터 저장 완료: {name}")
            return True
        except Exception as e:
            logger.error(f"데이터 저장 중 오류 발생: {e}")
            return False

    def get_all_faces(self):
        """저장된 모든 인물 데이터 반환 (임베딩 포함)"""
        faces = []
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name, embedding FROM faces")
                rows = cursor.fetchall()
                
                for row in rows:
                    name, emb_str = row
                    faces.append({
                        "name": name,
                        "embedding": json.loads(emb_str)
                    })
        except Exception as e:
            logger.error(f"데이터 로드 중 오류 발생: {e}")
        return faces

    def get_name_list(self):
        """저장된 인물 이름 목록만 반환"""
        names = []
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM faces")
                rows = cursor.fetchall()
                names = [row[0] for row in rows]
        except Exception as e:
            logger.error(f"이름 목록 로드 중 오류 발생: {e}")
        return names

    def delete_face(self, name):
        """인물 정보 삭제"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM faces WHERE name = ?", (name,))
                deleted = cursor.rowcount > 0
                conn.commit()
            
            if deleted:
                logger.info(f"SQLite에서 인물 삭제됨: {name}")
                return True
            return False
        except Exception as e:
            logger.error(f"인물 삭제 중 오류 발생: {e}")
            return False

    def log_access(self, name, liveness):
        """접근 내역 하나를 추가"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO access_history (name, liveness) VALUES (?, ?)", (name, liveness))
                conn.commit()
        except Exception as e:
            logger.error(f"접근 로그 기록 중 오류 발생: {e}")

    def get_recent_logs(self, limit=50):
        """최근 접근 내역 N개를 반환"""
        logs = []
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                # 최신 순 정렬
                cursor.execute("SELECT id, name, timestamp, liveness FROM access_history ORDER BY id DESC LIMIT ?", (limit,))
                rows = cursor.fetchall()
                for row in rows:
                    logs.append({
                        "id": row[0],
                        "name": row[1],
                        "timestamp": row[2],
                        "liveness": row[3]
                    })
        except Exception as e:
            logger.error(f"접근 로그 조회 중 오류 발생: {e}")
        return logs

# 싱글톤 인스턴스 생성
storage = FaceDataStorage()
