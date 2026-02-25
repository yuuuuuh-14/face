[🇰🇷 한국어 문서](11-project-tips.md)

# [11] Masterstroke of Design: Project Maintenance and Extension Tips

Designing a single system is not the end. These are the recommended operating policies when trying to create variations based on this project base (BCC).

## 1. Track Metrics
The `FPS` and `Latency(ms)` indicators exposed at the top of the Sci-Fi HUD screen or the browser debug console are not just for show.
- **Signal of Performance Degradation**: If you modified the model recognition module logic and the FPS suddenly dropped from 30 to 5, unconditionally rollback the code immediately (the main thread is blocked by a background thread).

## 2. Beware the Pitfall of File I/O Concurrency (Database Locks)
Currently, BCC uses `SQLite3` as its data engine. While it guarantees overwhelmingly superior concurrency compared to standard JSON, if dozens of users try to register their faces via POST API simultaneously, a DB Lock (`Database is locked` error) can occur.

**[Extension Suggestion]** If you wish to convert this for enterprise environment multi-connection clients, you must replace `SQLite` with a full RDBMS model like MySQL or PostgreSQL, or add Connection Pooling logic.

## 3. Control Resource Thresholds (CPU / Heat Suppression)
When this program runs, since it's an on-device model computation, your laptop fan will start screaming.
- **Importance of Defensive Logic**: If the `/api/stream` is in an idle phase where it's not being requested, it is recommended to advance the logic to Hibernate (temporarily stop) so that AI model inference does not cause frame waste. 

Keeping these design details and marginal costs in mind allows you to leap from a Coder to a Systems Engineer.
