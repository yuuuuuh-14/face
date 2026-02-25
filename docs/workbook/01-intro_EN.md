[🇰🇷 한국어 문서](01-intro.md)

# [01] BIOMETRIC_CONTROL_CENTER (BCC) Introduction and Philosophy

## 1. Project Background
Large-scale biometric systems (e.g., facial recognition access control) typically operate on vast cloud infrastructures, heavy Docker containers, and complex Relational Database Management Systems (RDBMS). Such structures can cause the following issues:
- **High Initial Barrier**: Takes days to set up the development environment.
- **Closed Nature**: Difficult for the system to operate in isolated (offline) environments disconnected from the external internet.
- **Data Management**: Over-specification expenditure for simple data persistence.

The project designed to counter this is the **BIOMETRIC_CONTROL_CENTER (BCC)**.
BCC is a hybrid dashboard that **boots instantly with just a laptop webcam without cloud connection**, boasting sophisticated recognition accuracy utilizing top-tier deep learning components (InsightFace).

## 2. Why a Sci-Fi HUD?
We determined that dashboards used by administrators don't always need to be boring and rigid. 
A **Cybernetic HUD (Heads-Up Display)** design inspired by Sci-Fi movies (Iron Man, Splinter Cell, etc.) offers the following advantages beyond mere visual flair:

1. **Enhanced Situational Awareness**: By utilizing neon-glow elements (overlay boxes, scan lines) on a black background to increase visual contrast, moving subjects (faces) can be tracked more intuitively.
2. **Rhythmic Feedback**: As myriad metadata flowing from real-time SSE (Server-Sent Events) is mapped onto the screen with animations, the system's operational status is transparently visualized.

## 3. Core Technological Philosophy
- **Zero-Config, Local-First**: Everything should work with just two launches: `app.py` and `yarn start`.
- **State as Files**: No database daemon is launched. Model snapshots and registered face vector information are all securely (and visibly) managed locally as `SQLite`/`JSON` files.
- **Non-blocking Pipeline**: The thread rendering the UI and the thread responsible for AI inference are physically completely separated, ensuring heavy AI computations do not cause the video feed (MJPEG) to lag.

From the next chapter, we will look at how these philosophies have been materialized into code.
