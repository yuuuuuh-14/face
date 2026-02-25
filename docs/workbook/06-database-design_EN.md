[🇰🇷 한국어 문서](06-database-design.md)

# [06] Database Architecture Design: SQLite Persistence Strategy

Even for a personal/short-term project rather than large enterprise software, data concurrency and integrity are always concerns.

BCC abandoned the previous pure JSON file overwrite method and adopted the lightweight yet powerful relational connection infrastructure of **SQLite Database (`data/faces.db`)**.

## 1. Benefits of SQLite-based File Storage Strategy
When the system runs, the Python backend forms a connection to the `/data/faces.db` file upon startup. At this time, everything works just with Python's built-in modules without needing to spin up a separate RDBMS engine.

- **Safe Concurrency**: In the previous JSON approach, there was a risk of file corruption (breaking) when multiple threads read and wrote simultaneously. SQLite supports its own locking mechanism, ensuring the persistent preservation of faces even during parallel data I/O.
- **Structural Schema**: 
  - `id`: Auto-increment Primary Key
  - `name`: Unique identifier word of the registered target (Automatic duplicate registration avoidance using the UNIQUE option - Upsert processing)
  - `embedding`: Converts (stringifies) the 512-dimensional array data of InsightFace into JSON format string for lossless insertion.
- **Transparent Yet Powerful Debugging**: Developers can safely visually verify, modify, and delete data at any time via DB tools like DataGrip, DBeaver, or the `sqlite3` CLI command.

## 2. Matching Process Optimization Strategy
Every time a new person appears on the camera, fetching and reading data from the `faces.db` file causes disk I/O, which could lead to lag in the camera frame.

To solve this, BCC adopted a method of **fetching data from SQLite, caching it in RAM memory as a dictionary, and comparing it by looping (for-loop)**. (A hybrid strategy taking both speed + integrity)

Thanks to SQLite, an ultra-lightweight DB based on a single file, Standalone Deployment is made possible without building Docker or any separate server environments.
