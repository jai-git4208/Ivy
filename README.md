# 🌸 Ivy — Local AI Agent with System Control

Ivy is a **personal AI agent** that runs **completely offline** on your machine.
She uses [Ollama](https://ollama.ai) to run LLMs locally, a Python backend for actions (like opening apps, typing, taking screenshots), and an **Electron orb UI** for interaction.

---

## ✨ Features

* 💻 **Runs locally** — no cloud, no data leaks.
* 🧠 **Powered by Ollama** (supports `gemma:4b`, `llama3`, etc.).
* 🎤 **Speech recognition** (optional) — Ivy can listen to your voice.
* 🔊 **Text-to-Speech (TTS)** — Ivy speaks back naturally.
* 🖥️ **System control** (via Python):

  * `open_app` → launch desktop apps (Chrome, VS Code, File Manager, etc.)
  * `keyboard_action` → type text, send hotkeys, press enter
  * `click_action` → click on-screen positions
  * `scroll_action` → scroll up/down
  * `take_screenshot` → capture and save a screenshot
* 🌌 **Beautiful UI** — animated gradient orb powered by Electron.js.
* ⚡ **Spacebar trigger** — press space to launch Ivy instantly.

---

## 🚀 Getting Started

### 1. Install dependencies

Make sure you have:

* **Python 3.10+** with `venv`
* **Node.js + npm**
* **Ollama** installed and running
* System utilities: `xdotool`, `gnome` apps (for app launching)
* Python packages:

  ```bash
  pip install -r requirements.txt
  ```

### 2. Clone the repo

```bash
git clone https://github.com/your-username/Ivy.git
cd Ivy
```

### 3. Setup virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Create Ivy model with Ollama

From the project root:

```bash
ollama create Ivy -f Modelfile
```

### 5. Run backend (Python)

```bash
python app.py
```

### 6. Run frontend (Electron UI)

```bash
cd frontend
npm install
npm start
```

---

## 🎮 Usage

* Start **Electron orb UI** (`npm start`).
* Press **Spacebar** → orb animates + Ivy starts listening.
* Say or type a command → Ivy parses it with her LLM → executes Python action → speaks back.

### Example commands:

* `open chrome` → launches Google Chrome
* `type Hello World` → types into focused window
* `take screenshot` → saves a screenshot in `/home/jaimin-pansal/Ivy/screenshot.png`
* `press ctrl+c` → sends hotkey

---

## 🛠️ Tech Stack

* **AI backend** → [Ollama](https://ollama.ai)
* **LLM** → `gemma:4b` (custom Ivy build)
* **System actions** → Python (`subprocess`, `pyautogui`, `xdotool`)
* **TTS** → Murf API (with local pyttsx3 fallback)
* **Speech Recognition** → `speech_recognition`
* **UI** → Electron.js + Vanilla JS (Gradient Orb Animation)

---

## 🔮 Roadmap

* [ ] Smarter **context memory**
* [ ] Offline neural TTS for natural voice
* [ ] Offline web search integration
* [ ] More desktop automations (file manager, notifications, etc.)
* [ ] Packaged cross-platform installer

---

## 🤝 Contributing

PRs and ideas are welcome! Fork this repo, hack Ivy, and share improvements.

---

## 📜 License

Apache 2.0 License © 2025 Jaimin Pansal

---

Made with ❤️ by **Jaimin**

