# Ivy

> A privacy-first, offline AI assistant that runs entirely on your local machine

**"Your data should stay yours. Period."**

In an era where AI assistants send everything you say to distant servers, Ivy takes a different approach. She lives on your machine, thinks on your hardware, and never phones home. This is AI assistance without compromise—powerful, intelligent, and completely private.

## Table of Contents

- [The Story Behind Ivy](#the-story-behind-ivy)
- [Overview](#overview)
- [Architecture](#architecture)
- [Key Features](#key-features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Development](#development)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## The Story Behind Ivy

Every time you ask Alexa about the weather, your voice travels to Amazon's servers. When you tell Siri to set a reminder, Apple hears it too. Google Assistant? Your conversations are fuel for their algorithms. This is the bargain we've accepted: convenience in exchange for privacy.

But what if we didn't have to choose?

Ivy was born from a simple question: **"Can I build an AI assistant that never leaves my computer?"** Not because of paranoia, but because of principle. Your thoughts, your commands, your daily routines—these are yours. They shouldn't be the price of admission for using modern technology.

The challenge was real. Cloud-based assistants are powerful because they leverage massive data centers and billions of training examples. How could a local assistant compete?

The answer arrived with the open-source AI revolution. Models like Llama and Gemma proved that sophisticated language understanding could run on consumer hardware. Ollama made it practical. Suddenly, the dream of a truly private AI assistant wasn't just possible—it was achievable.

Ivy represents more than code. She's a statement: **technology should serve you, not surveil you.** She's proof that you can have intelligent assistance without sacrificing your digital privacy. And she's an invitation to others who believe that the future of AI should be open, local, and under your control.

## Overview

Ivy is a sophisticated personal AI agent designed for complete privacy and offline operation. Built on Ollama for local LLM inference, Ivy combines natural language processing with system-level automation capabilities, all wrapped in an elegant Electron-based user interface.

### The Problem Ivy Solves

Modern AI assistants are incredibly capable, but they come with hidden costs:

- **Privacy Erosion**: Every interaction is logged, analyzed, and stored on corporate servers
- **Internet Dependency**: No connection means no assistant, even for simple tasks
- **Data Vulnerability**: Your personal information sits in databases you don't control
- **Vendor Lock-in**: Switching platforms means losing all your history and preferences

Ivy addresses each of these issues:

- **Zero Cloud Dependency**: Everything runs locally—your data never leaves your machine
- **Offline Operation**: Full functionality without internet connectivity
- **Complete Control**: You own the data, the model, and the infrastructure
- **Open Source Freedom**: Modify, extend, or fork without restrictions

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Electron UI Layer                                  │
│  ┌─────────────────────────────────────────────────────┐     │
│  │  Gradient Orb Interface (JavaScript/CSS)                      │     │
│  │  - Visual feedback                                            │     │
│  │  - Spacebar activation                                        │     │
│  └─────────────────────────────────────────────────────┘     │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ IPC Communication
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                   Python Backend (Flask)                                │
│  ┌─────────────────────────────────────────────────────┐      │
│  │  Natural Language Processing                                  │      │
│  │  ┌───────────────────────────────────────────────┐   │      │
│  │  │     Ollama LLM (gemma:4b/llama3)                       │   │      │
│  │  │     Custom Modelfile: "Ivy"                            │   │      │
│  │  └───────────────────────────────────────────────┘.  │      │
│  └─────────────────────────────────────────────────────┘      │
│  ┌─────────────────────────────────────────────────────┐      │
│  │  Action Execution Layer                                       │      │
│  │  - Application Control (subprocess)                           │      │
│  │  - Keyboard/Mouse Automation (pyautogui, xdotool)             │      │
│  │  - Screenshot Capture                                         │      │
│  └─────────────────────────────────────────────────────┘      │
│  ┌─────────────────────────────────────────────────────┐      │
│  │  I/O Processing                                               │      │
│  │  - Speech Recognition (speech_recognition)                    │      │
│  │  - Text-to-Speech (Murf API / pyttsx3)                        │      │
│  └─────────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

### The Design Philosophy

Ivy's architecture reflects three core principles:

1. **Local-First**: Every component can function without external dependencies
2. **Modular**: Each layer is independent, making customization and debugging straightforward
3. **Transparent**: Open source means you can see exactly what Ivy does with your data (spoiler: nothing)

## Key Features

### Privacy & Security: The Foundation

**100% Offline Operation**  
Ivy processes everything locally. Your commands go from your keyboard to your CPU to your screen. No intermediate stops. No cloud servers. No data centers. Your conversations with Ivy are as private as your thoughts.

**No Cloud Dependencies**  
Internet goes down? Ivy keeps working. Traveling somewhere without WiFi? Ivy's still there. Don't want to share your data? Ivy never asks.

**No Data Logging**  
Unless you explicitly save something, it's gone. Ivy doesn't keep transcripts, doesn't build profiles, doesn't remember what you did last week. Each session is a clean slate.

### AI Capabilities: Intelligence Without Compromise

**Local LLM Inference**  
Powered by Ollama, Ivy runs capable language models directly on your hardware. Whether you choose the efficient gemma:4b or the more powerful llama3, the intelligence is yours to command—and control.

**Custom Model Configuration**  
Through the Modelfile, you define who Ivy is. Want a formal assistant? A casual companion? A technical expert? You write the system prompt, you shape the personality.

**Context-Aware Responses**  
Ivy understands natural language in context. "Open Chrome and search for Python tutorials" isn't two commands—it's one intention that Ivy parses and executes intelligently.

### System Integration: Your Computer, Your Control

**Application Launcher**  
"Open Chrome." "Launch VS Code." "Start the file manager." Ivy knows your applications and brings them to life with a word.

**Keyboard Automation**  
Need to type a long email template? Have a complex keyboard shortcut? Ivy handles the tedious typing and key combinations so you don't have to.

**Mouse Control**  
Click specific coordinates, automate UI interactions, or navigate interfaces programmatically. If you can see it, Ivy can click it.

**Screenshot Capture**  
Document your work, capture moments, or save reference images with a simple voice command.

### User Interface: Beauty Meets Function

**Animated Gradient Orb**  
Forget boring chat boxes. Ivy presents herself as a living, breathing orb of shifting colors. It's not just aesthetic—the orb's animation tells you exactly what Ivy's doing at any moment.

**Spacebar Activation**  
No wake words to remember, no buttons to find. Press space, Ivy listens. It's muscle memory from day one.

**Visual Feedback**  
The orb pulses when listening, shimmers while thinking, and glows when speaking. You always know Ivy's state without reading a single word.

### Voice Interaction: Speak Naturally

**Speech Recognition**  
Ivy can hear you. Optional voice input means hands-free operation when typing isn't convenient.

**Natural Text-to-Speech**  
Ivy speaks back with natural-sounding voices through Murf API, with a pyttsx3 fallback that ensures she's never silent when you need her.

## System Requirements

### Operating System
- Linux (primary support with xdotool and GNOME)
- Planned: Windows and macOS compatibility

### Software Dependencies
- Python 3.10 or higher
- Node.js 14.x or higher (with npm)
- Ollama (installed and running)

### System Utilities
- `xdotool`: X11 automation tool
- GNOME desktop applications (for app launching)

### Python Packages
See `requirements.txt` for complete list:
- Flask (web server)
- speech_recognition (voice input)
- pyautogui (automation)
- pyttsx3 (text-to-speech fallback)
- requests (API communication)

## Installation

Getting Ivy up and running is straightforward. This is a local installation—no accounts to create, no API keys to juggle (unless you want Murf TTS), no cloud services to configure.

### 1. Clone the Repository

```bash
git clone https://github.com/jai-git4208/Ivy.git
cd Ivy
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Configure Ollama Model

```bash
# Create custom Ivy model from Modelfile
ollama create Ivy -f Modelfile
```

The Modelfile contains custom system prompts that define Ivy's personality and capabilities. This is where you can customize how Ivy thinks and responds. Ensure Ollama is running before executing this command.

### 4. Install Frontend Dependencies

```bash
cd frontend
npm install
```

### 5. System Utilities (Linux)

```bash
# Install xdotool for automation
sudo apt-get install xdotool

# Verify GNOME applications are installed
which gnome-terminal
```

**That's it.** No registration, no email confirmation, no privacy policy to accept. Ivy is installed and she's yours.

## Configuration

### Model Selection: Choosing Ivy's Brain

Edit the `Modelfile` to customize Ivy's behavior or switch between different base models:

```dockerfile
FROM gemma:4b

SYSTEM """
You are Ivy, a helpful personal AI assistant...
"""
```

**Model Options:**
- `gemma:4b`: Lightweight and efficient—perfect for most tasks without taxing your hardware
- `llama3`: More capable and nuanced—ideal if you have the processing power and want deeper reasoning
- Any other Ollama-compatible model: Experiment and find what works for you

The SYSTEM prompt is Ivy's personality. This is where you teach her how to interpret commands, how to respond, and what kind of assistant she should be. Make her formal or casual, verbose or concise, technical or accessible. She's your creation.

### Speech Recognition

Configure microphone settings in `app.py`:

```python
# Adjust recognition parameters
recognizer.energy_threshold = 4000  # Sensitivity to ambient noise
recognizer.pause_threshold = 0.8     # How long to wait before assuming you're done speaking
```

### Text-to-Speech

Configure TTS settings:

```python
# Murf API configuration (primary)
MURF_API_KEY = "your_api_key_here"

# pyttsx3 fallback settings (completely offline)
engine.setProperty('rate', 150)     # Speaking speed
engine.setProperty('volume', 0.9)   # Volume level
```

### Screenshot Location

Default path: `/home/jaimin-pansal/Ivy/screenshot.png`

Update in `app.py` as needed:

```python
SCREENSHOT_PATH = "/your/custom/path/screenshot.png"
```

## Usage

### Starting Ivy

**Terminal 1: Start Backend Server**

```bash
cd Ivy
source venv/bin/activate
python app.py
```

The Flask server will start on `http://localhost:5000`. This is Ivy's brain coming online.

**Terminal 2: Start Frontend UI**

```bash
cd frontend
npm start
```

The Electron window launches, and there she is—a pulsing gradient orb, ready to help.

### Your First Interaction

Press the spacebar. The orb responds immediately, shifting its colors to let you know it's listening. Say or type: "Open Chrome."

Ivy processes your command through her local LLM, understands your intent, and launches Google Chrome. No lag while waiting for a server response. No "I didn't quite get that" because your internet hiccupped. Just immediate, intelligent action.

### Interaction Methods

**Spacebar Activation**  
The spacebar is your trigger. One press, and Ivy's attention is yours. The orb animates, indicating she's listening. Speak your command or type it—Ivy handles both.

**Voice Commands**  
If you've enabled speech recognition, just talk naturally. "Open Chrome." "Type my email signature." "Take a screenshot." Ivy understands conversational language, not rigid command syntax.

**Text Commands**  
Prefer typing? No problem. Type your command directly when prompted, and Ivy responds just as intelligently.

### Example Commands

| Command | Action | Result |
|---------|--------|--------|
| `open chrome` | Application launcher | Launches Google Chrome browser |
| `open vscode` | Application launcher | Launches Visual Studio Code |
| `type Hello World` | Keyboard automation | Types "Hello World" into active window |
| `press ctrl+c` | Keyboard shortcut | Sends Ctrl+C key combination |
| `press enter` | Keyboard action | Presses Enter key |
| `take screenshot` | Screen capture | Saves screenshot to configured path |
| `scroll up` | Mouse automation | Scrolls content upward |
| `click 500 300` | Mouse automation | Clicks at coordinates (500, 300) |

### Real-World Scenarios

**The Morning Routine**  
"Open Spotify, then Chrome, then my email." Ivy launches each application in sequence, getting your workday started while you're still finishing your coffee.

**The Quick Screenshot**  
You're on a video call and someone shares something important. "Take a screenshot." Done. No fumbling for Print Screen or opening screenshot tools.

**The Lazy Typing**  
You need to fill out a form with your standard information. "Type my full name and address." Ivy does the tedious work while you focus on the important stuff.

## Technical Details

### Backend Architecture

**Flask Server (`app.py`)**  
The heart of Ivy's logic. Flask handles incoming commands, routes them to the appropriate action handlers, and manages communication between the UI and the system.

**Action Handlers**
```python
def open_app(app_name):
    """Launch desktop application"""
    subprocess.Popen([app_name])

def keyboard_action(text=None, hotkey=None):
    """Execute keyboard actions"""
    if text:
        pyautogui.write(text)
    elif hotkey:
        pyautogui.hotkey(*hotkey.split('+'))

def click_action(x, y):
    """Perform mouse click"""
    pyautogui.click(x, y)

def take_screenshot():
    """Capture and save screenshot"""
    screenshot = pyautogui.screenshot()
    screenshot.save(SCREENSHOT_PATH)
```

**Ollama Integration**
```python
def process_with_llm(user_input):
    """Send input to local LLM for processing"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "Ivy",
            "prompt": user_input,
            "stream": False
        }
    )
    return response.json()
```

### Frontend Architecture

**Electron Main Process**  
Manages the application window, handles IPC communication with the renderer process, and can integrate with the system tray for quick access.

**Renderer Process (UI)**  
The visual layer. The gradient orb is rendered using CSS animations and potentially WebGL for more complex effects. State updates happen in real-time based on backend responses.

**Gradient Orb Animation**
```javascript
// Simplified representation
const orb = {
    states: ['idle', 'listening', 'processing', 'speaking'],
    animate: function(state) {
        // Apply corresponding CSS animation
        element.className = `orb-${state}`;
    }
};
```

### Communication Flow

This is how a command travels through Ivy's system:

```
User Input (Voice/Text)
        │
        ▼
Electron UI (captures input)
        │
        ▼
Flask Backend (receives via IPC/HTTP)
        │
        ▼
Ollama LLM (processes natural language)
        │
        ▼
Action Parser (extracts intent and parameters)
        │
        ▼
Action Executor (performs system operation)
        │
        ▼
Response Generator (formats output)
        │
        ▼
TTS Engine (converts to speech if enabled)
        │
        ▼
Electron UI (displays/plays response)
```

Every step happens on your machine. The data never leaves this loop.

## Development

### Project Structure

```
Ivy/
├── app.py                  # Flask backend server
├── Modelfile              # Ollama model configuration
├── requirements.txt       # Python dependencies
├── frontend/             # Electron application
│   ├── package.json
│   ├── main.js           # Electron main process
│   ├── script.js       # UI logic
│   ├── index.html        # Main UI structure
│   └── styles.css.       # Gradient orb styling
│             
├── venv/                 # Python virtual environment
└── README.md
```

### Adding New Actions

Extending Ivy is straightforward. Here's how to add a new capability:

**1. Define action function in `app.py`:**

```python
def new_action(param1, param2):
    """Description of new action"""
    # Implementation
    pass
```

**2. Add route endpoint:**

```python
@app.route('/api/new-action', methods=['POST'])
def handle_new_action():
    data = request.json
    result = new_action(data['param1'], data['param2'])
    return jsonify({'success': True, 'result': result})
```

**3. Update LLM prompt in Modelfile:**

```dockerfile
SYSTEM """
...
- new_action: Description and usage
...
"""
```

**4. Register in frontend (if needed):**

```javascript
async function executeNewAction(params) {
    const response = await fetch('http://localhost:5000/api/new-action', {
        method: 'POST',
        body: JSON.stringify(params)
    });
    return response.json();
}
```

### Testing

```bash
# Test backend
python -m pytest tests/

# Test specific action
python -c "from app import open_app; open_app('firefox')"

# Lint code
pylint app.py
flake8 app.py
```

## Roadmap

Ivy is just beginning. Here's where she's headed:

### Intelligence Enhancements
- **Extended context memory**: Ivy remembers your conversation within a session, building understanding as you work together
- **Learning from preferences**: Over time, Ivy adapts to your patterns and anticipates your needs
- **Proactive suggestions**: Instead of just responding, Ivy offers helpful suggestions based on your workflow

### Voice & Audio
- **Offline neural TTS**: Higher quality, more natural-sounding voices without any API dependency
- **Custom wake word**: "Hey Ivy" could activate her from anywhere in your system
- **Multiple voice profiles**: Different voices for different contexts or moods

### System Integration
- **File manager operations**: Create, move, organize, and delete files through natural language
- **System notifications**: Ivy can notify you of events, reminders, or important information
- **Calendar and reminder management**: "Remind me tomorrow at 3 PM" becomes a reality
- **Email client integration**: "Send an email to..." without opening your email client

### Search & Information
- **Offline web search**: Index and search web content locally without live internet
- **Document search and retrieval**: "Find that report I wrote last month" actually works
- **Wikipedia offline**: Access the sum of human knowledge without connectivity

### Platform Support
- **Windows compatibility**: Bring Ivy to the majority of desktop users
- **macOS native support**: Native integration with Apple's ecosystem
- **Cross-platform installer**: One-click installation for all platforms

### Developer Features
- **Plugin system**: Build and share custom actions without modifying core code
- **API for third-party integrations**: Let other applications leverage Ivy's capabilities
- **Configuration GUI**: Manage settings visually instead of editing config files

## Contributing

Ivy is open source for a reason. If you believe in private, local-first AI, your contributions can help make that vision a reality for everyone.

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes** with clear, descriptive commits
4. **Test thoroughly** to ensure nothing breaks
5. **Submit a pull request** with a detailed description

### Contribution Guidelines

- Follow existing code style and conventions
- Add tests for new features
- Update documentation as needed
- Keep commits focused and atomic
- Write clear commit messages

### Areas for Contribution

- Cross-platform compatibility (Windows/macOS)
- New action types and system integrations
- UI/UX improvements
- Documentation and tutorials
- Bug fixes and performance optimizations
- Test coverage expansion

Every contribution, no matter how small, moves us toward a future where AI assistance doesn't require surrendering your privacy.

## License

```
Copyright 2025 Jaimin Pansal

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## Acknowledgments

- **Ollama**: For proving that powerful AI can run on consumer hardware
- **Electron**: For making beautiful, cross-platform interfaces accessible
- **Python Community**: For the tools that make system automation possible
- **The Open Source Community**: For believing that technology should be open and accessible

## Contact & Support

- **Author**: Jaimin Pansal
- **Repository**: [github.com/jai-git4208/Ivy](https://github.com/jai-git4208/Ivy)
- **Issues**: Report bugs and request features via GitHub Issues

## Final Thoughts

In a world where "AI assistant" has become synonymous with "surveillance device," Ivy represents an alternative path. She's not perfect—local models aren't as capable as their cloud-based counterparts, and running everything locally takes more setup than just downloading an app.

But Ivy offers something those other assistants can't: **certainty**. Certainty that your commands aren't being logged. Certainty that your routines aren't being analyzed. Certainty that your data is yours, sitting on your disk, under your control.

Ivy is a bet that privacy matters. That local-first software is worth the extra effort. That we can build intelligent systems without compromising our values.

If you agree, welcome. Let's build something better together.

---

**Note**: This project is under active development. Features and documentation are subject to change. Always refer to the latest release for stable functionality.
