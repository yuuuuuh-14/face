[🇰🇷 한국어 문서](09-ai-instructions.md)

# [09] Collaborative Communication in the Generative AI Era (Prompt Engineering in BCC)

Maintaining a mid-to-large scale project combined with Angular, Flask, InsightFace, and SSE networks like BIOMETRIC_CONTROL_CENTER (BCC) alone is never easy.
This is a strategic guide on **"how to ask the right questions"** to the latest Large Language Models (LLM - ChatGPT, Claude, Gemini) when understanding and modifying code.

## 1. Terrible Prompt Patterns:
> ❌ **Beginner's Question**: "The box color isn't showing up over the camera screen in Angular. Fix the code."

Because the LLM is a blank slate regarding whether the project's premise relies on local JSON, or if the communication is Polling or SSE, it will write completely bogus code.

## 2. Perfect Prompt Structure (The BCC Prompt Template)
Explicitly inject into the LLM what kind of worldview (Context) it has been thrown into.

> ✅ **Master's Question**:
> "Modify the code based on the following constraints.
> 
> **[Context]**
> - **Project Name**: BIOMETRIC_CONTROL_CENTER
> - **Stack**: Angular Frontend and Flask Backend (using SQLite local DB)
> - **Core Logic**: The backend is pushing face bounding boxes via real-time SSE (Server-Sent Events) from `app.py` on port 8001, and the frontend catches these events to overlay markers on SVG.
> - **Current Situation**: I want to add one more attribute, the predicted age of the target, to the data packet (`{"faces": [{"bbox": [1,2,3,4], "name": "..."}]}`) sent from the backend.
> 
> **[Goal]**
> 1) Modify the Python serialization part in the Flask source code.
> 2) Update the RxJS observer interface layer (TypeScript) of the Angular component."

By specifying like this, the LLM will instantly present you with the ideal thread logic and RxJS refactored version tailored to the project architecture. **By thoroughly grasping the contents of chapters 1 to 6 of this workbook, your ability to inject context will naturally improve.**
