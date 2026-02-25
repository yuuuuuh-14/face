[🇰🇷 한국어 문서](WORKBOOK.md)

# 📚 BIOMETRIC_CONTROL_CENTER (BCC) Learning Workbook

This workbook is an **official step-by-step guide** for analyzing the BCC project's source code and understanding its structure.
Going beyond simply copying code, it delves deeply into the design philosophy of **'Why was this built with this technology (Why)'**.

## 🗂️ Chapter Directory (Index)

This is the root table of contents. You can enter detailed learning documents (`docs/workbook/*_EN.md`) by clicking each item.

---

### [Part 1] Project Essence and Foundational Knowledge
1. **[01-intro.md](./workbook/01-intro_EN.md) (Introduction)**
   - The reason for the system's existence, the philosophy embedded in the Sci-Fi HUD design, and the justification for local-first operation.
2. **[02-first-principles.md](./workbook/02-first-principles_EN.md) (Computer Vision and Foundational Principles)**
   - The essence of MJPEG streaming, why rely on simple image frame transmission.
   - The clear technical difference between facial 'Detection' and 'Recognition'.

---

### [Part 2] Architecture and Distributed Layer Network
3. **[03-project-structure.md](./workbook/03-project-structure_EN.md) (Structure Analysis)**
   - Event communication pipeline spanning Frontend (Angular) ↔ Backend (Flask) ↔ Data (SQLite).
4. **[04-backend-stack.md](./workbook/04-backend-stack_EN.md) (AI Threading and Backend)**
   - Python multi-threading/GIL limitations and means to overcome frame latency.
   - A closer look at the Cosine Similarity calculation mechanism.
5. **[05-frontend-stack.md](./workbook/05-frontend-stack_EN.md) (Rendering and HUD Viewer)**
   - Angular single-page canvas rendering optimization techniques (Change Detection tuning).
   - CSS animation techniques to minimize the load of the Glow effect.
6. **[06-database-design.md](./workbook/06-database-design_EN.md) (Persistent Storage Architecture Design)**
   - Reasons for abandoning heavy RDBMS and opting for SQLite storage, and Trade-off analysis.

---

### [Part 3] Development History and Collaboration
7. **[07-deployment.md](./workbook/07-deployment_EN.md) (Environment Isolation and Operation Principles)**
   - Understanding the Linux/Windows virtual environment paradigm.
8. **[08-phase-guide.md](./workbook/08-phase-guide_EN.md) (Milestone Memoir)**
   - The evolutionary process spanning from project release Phase 1 to Phase 4.
9. **[09-ai-instructions.md](./workbook/09-ai-instructions_EN.md) (Utilizing Generative AI Context)**
   - How to effectively explain system context to LLMs (Claude, ChatGPT, Gemini, etc.) for next-generation coding.

---

### [Part 4] Operational Guidelines (Ops)
10. **[10-troubleshooting.md](./workbook/10-troubleshooting_EN.md) (Disaster Response Manual)**
    - Methods for resolving common Python dependency hells, countermeasures for camera socket errors.
11. **[11-project-tips.md](./workbook/11-project-tips_EN.md) (Project Tips & Tricks)**
    - Securing code extensibility and maintainability.
12. **[12-quick-reference.md](./workbook/12-quick-reference_EN.md) (Cheat Sheet)**
    - A collection of key commands for Angular, Flask, Yarn, and Pip.
13. **[13-final-advice.md](./workbook/13-final-advice_EN.md) (Conclusion)**
    - Final ideological advice for architects.

---

## 🛤️ Recommended Learning Paths by Reader Type

- **'I just want to hack and rewrite this code my way' (Rapid Hacking Mode)**
  - `03-project-structure_EN.md` ➡️ `10-troubleshooting_EN.md` ➡️ `12-quick-reference_EN.md`
- **'I want to know the architecture of why it was developed this way without using Docker' (Architect Mode)**
  - `01-intro_EN.md` ➡️ `02-first-principles_EN.md` ➡️ `04-backend-stack_EN.md` ➡️ `06-database-design_EN.md`
