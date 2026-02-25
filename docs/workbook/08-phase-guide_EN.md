[🇰🇷 한국어 문서](08-phase-guide.md)

# [08] Project Evolution: Retrospective Guide by Phase

Until BIOMETRIC_CONTROL_CENTER (BCC) reached the v3.5 Stable version, the development phases were a journey of fusing fragmented technologies into one.

## Phase 1: Return to Local (The Great Escape)
- **Overview**: When first planning this baby, we split the modules into multiple trendy Docker containers, but eventually got exhausted trying to punch through camera passthroughs and forwarding X11 displays.
- **Achievement**: Brought the entire backend down to a local native environment (Python Venv-based `app.py`). This increased development productivity by more than **10 times** and minimized lag with a primitive structure that directly streams MJPEG from OpenCV. 

## Phase 2: Recognize 'Me' (Identity Persistence)
- **Overview**: We drew square boxes nicely on the screen, but the system didn't know how to distinguish people. We had to introduce a "Person Registration" feature.
- **Achievement**: Instead of a heavy PostgreSQL server, a completely file-based embedded `SQLite` DB was adopted. By cramming serialized data of face vectors into `faces.db`, caching them in memory, and performing cosine matching, we secured both integrity and speed.

## Phase 3: Style is Everything (Sci-Fi Cybernetic UI)
- **Overview**: The existing frontend buttons and screens felt too much like a bank/shopping mall. We wanted 'that thing' of secret agents in movies.
- **Achievement**: Completely rebuilt the JavaScript into an Angular workspace format. Abandoned Tailwind's utility and ground in hardcoded SCSS properties to equip neon glow scanline effects and Material dialog modals. 

## Phase 4 (In Progress): Deep Intelligence Layer
- **Achievement**: Beyond simple matching, bypassed/extended the pipeline to extract additional squad attributes (Gender, Age) from InsightFace. Currently undergoing refactoring to catch memory leaks that spew meaningless errors and to advance the Python-based async thread monitoring system.
