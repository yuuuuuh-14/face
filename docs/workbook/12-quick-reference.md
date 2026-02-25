[🌐 EN VERSION](12-quick-reference_EN.md)

# [12] 전술 치트 시트 (Quick Status Reference)

BCC 프로젝트를 디버그하고 유지하기 위해 필요한 명령어 및 API 백과 요약본입니다.
외울 필요는 없으며 자주 들여다 보십시오.

## 터미널 코맨드 (Terminal Commands)

```bash
# === 강력 삭제 명령어: 파이썬 가상환경 완전 날리기 ===
# (의존성 꼬여서 답도 없을때 쓰는 최후의 수단. 이후 다시 설치)
rm -rf backend/venv

# === Angular 의존성 완전 날리기 ===
rm -rf frontend/node_modules
rm -rf frontend/dist

# === 파이썬 요구사항 다시 깔기 ===
cd backend
source venv/bin/activate
pip install -r ../requirements.txt
```

---

## B.C.C 핵심 API 엔드포인트 도면 (Backend 8001)

모든 데이터는 Flask 서버(Port 8001)를 중심으로 흘러나갑니다. 프론트엔드 코드는 이 명세서와 맵핑되어 있습니다.

### 🌐 [통신 채널] `GET /api/stream`
- **목적**: 무한 지연 이벤트(JSON) 발송기 (SSE)
- **페이로드 구조**: `{"faces": [ {"bbox": [...], "name": "Admin", "age": 31} ], "fps": 29 }`
- **수단**: Angular 내장된 `EventSource` 로 소켓 구독

### 🎥 [스트리밍 채널] `GET /api/video_feed`
- **목적**: 카메라 이미지(MJPEG) 무한 루프 스트리밍
- **수단**: 브라우저 `img` 태그의 `src` 주소로 하드코딩

### 🛡️ [명령 제어] `POST /api/register`
- **목적**: 인물 벡터 로컬 등록 추가 지시
- **바디**: `{ "name": "등록할 요원 이름" }`
- **비고**: 서버는 현재 스레드 메모리에 떠있는 찰나의 벡터를 즉시 매핑시켜 JSON 파일 재전송.

### 🛡️ [명령 제어] `GET /api/faces`
- **목적**: 등록된 디렉토리 목록(JSON Array) 가져와서 화면에 출력

### 🛡️ [명령 제어] `DELETE /api/delete_face`
- **목적**: 특정 이름의 요원 말소
- **바디**: `{ "name": "삭제할 요원 이름" }`
