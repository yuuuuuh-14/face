[🇰🇷 한국어 문서](07-deployment.md)

# [07] Deployment and the Mental Model of Virtual Environments (Mental Model for Python Env)

While a large enterprise production would naturally use Kubernetes or Docker Swarm, the top priority for **BIOMETRIC_CONTROL_CENTER (BCC)** is to operate instantly on a local computer (laptop).

To adhere to this principle without polluting the system, you must firmly understand the **"Virtual Environment"** paradigm of the Python ecosystem.

## 1. Global Python Hell
The most common mistake beginners make is blindly typing `pip install opencv-python insightface flask` into the terminal.
If this happens, all packages get mixed into the OS's built-in main Python environment. When you run another project tomorrow (e.g., a Django app), version conflicts will occur, ruining everything.

## 2. Setting up a Barrier: `python -m venv venv`
From Python 3 onwards, a module called `venv` is built-in. Navigate to the `backend` subdirectory within the root project and execute `python -m venv venv`.

- The folder named `venv/` itself (Visual Studio Code or PyCharm automatically avoids this folder) completely clones a new Python interpreter (`python.exe`) and package repository (`site-packages`) inside.
- **Activate**: Typing `source venv/bin/activate` (Mac/Linux) or `.\venv\Scripts\activate` (Windows) triggers this magic. If `(venv)` in parentheses appears at the top of the terminal command line, all subsequent `pip` and `python` commands you type will escape the OS and hover within this isolated folder.

## 3. Git Pollution Defense: `.gitignore`
Dozens of packages taking up gigabytes (GB) are installed inside the virtual environment. If you `git commit` this, a terrible tragedy will ensue.
This is why `venv/` is strongly blocked at the very top of the root `.gitignore` file.
We share only the "blueprint" called `requirements.txt` to the Git repository, not the virtual environment artifacts.

> Tip: The same logic applies to the frontend's `node_modules` for Git isolation. The foundation of Angular and Flask development starts with clarifying subjects to be excluded from version control.
