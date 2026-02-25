[🌐 EN VERSION](09-ai-instructions_EN.md)

# [09] 생성형 AI 시대의 협업 통신 (Prompt Engineering in BCC)

BIOMETRIC_CONTROL_CENTER (BCC) 처럼 Angular, Flask, InsightFace, SSE 통신망이 결합된 중규모 이상의 프로젝트를 혼자서 유지 보수하는 것은 결코 쉽지 않습니다.
코드를 이해하고 수정할 때 최신 거대 언어 모델(LLM - ChatGPT, Claude, Gemini)에게 **"어떻게 올바른 질문을 던질 것인가"** 에 대한 전략 가이드입니다.

## 1. 끔찍한 프롬프트 패턴:
> ❌ **초보자의 질문**: "Angular에서 카메라 화면 위에 박스 색상이 안 나와. 코드 고쳐줘."

LLM은 프로젝트의 전제가 로컬 JSON 에 의존하는지, 통신이 Polling 인지 SSE 인지 백지 상태이기 때문에 완전히 엉터리 코드를 작성해주게 됩니다.

## 2. 완벽한 지시어 구조 (The BCC Prompt Template)
LLM 에게 현재 자신이 어떤 세계관(Context)에 던져졌는지 명시적으로 주입하십시오.

> ✅ **마스터의 질문**:
> "다음 제약 조건을 기반으로 코드를 수정해줘.
> 
> **[Context]**
> - **프로젝트 명**: BIOMETRIC_CONTROL_CENTER
> - **스택**: Angular 프론트엔드와 Flask 백엔드 (SQLite 로컬 DB 사용)
> - **핵심 로직**: 백엔드는 8001 포트에서 `app.py` 가 실시간 SSE(Server-Sent Events) 로 얼굴 바운딩 박스를 밀어주고 있고, 프론트엔드는 이 이벤트를 잡아서 SVG에 마커를 오버레이 해.
> - **현재 상황**: 백엔드에서 전송하는 데이터 패킷(`{"faces": [{"bbox": [1,2,3,4], "name": "..."}]}`)에 타겟의 예측 나이 속성을 하나 더 추가하고 싶어.
> 
> **[Goal]**
> 1) Flask 소스코드 중 Python 직렬화 부분을 수정해 주고
> 2) Angular 컴포넌트의 RxJS 옵저버 인터페이스 계층(TypeScript)을 업데이트 해줘."

이처럼 명시하면, LLM은 프로젝트 아키텍처에 맞는 이상적인 스레드 로직과 RxJS 리팩토링 버전을 당신에게 단숨에 선물할 것입니다. **이 워크북 1장~6장의 내용을 잘 숙지하면 컨텍스트를 주입하는 능력이 자연스럽게 길러집니다.**
