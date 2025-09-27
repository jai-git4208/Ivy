import subprocess
import time
import pyautogui

# Dictionary of known apps with their command names
KNOWN_APPS = {
    "chrome": "google-chrome",
    "firefox": "firefox",
    "vscode": "code",
    "file_manager": "nautilus",
    "terminal": "gnome-terminal",
    "spotify": "spotify"
}

# Configure pyautogui
pyautogui.FAILSAFE = True  # Move mouse to top-left corner to abort
pyautogui.PAUSE = 0.1  # Default pause between actions

def keyboard_action(action: str, text: str = "", keys: str = "", delay: float = 0.1, wait_time: float = 0):
    """
    Performs keyboard actions using xdotool (Ubuntu/Linux).
    action: 'type', 'keys', or 'type_enter'
    text: text to type (for 'type' and 'type_enter')
    keys: key combination (for 'keys', e.g., 'ctrl+c', 'alt+Tab', 'F5')
    delay: delay between characters (only applies to typing)
    wait_time: delay before executing (in seconds)
    """
    try:
        if wait_time > 0:
            time.sleep(wait_time)

        if action == "type":
            if not text:
                return "No text provided to type."
            subprocess.run(["xdotool", "type", "--delay", str(int(delay*1000)), text])
            return f"Successfully typed: '{text}'"

        elif action == "keys":
            if not keys:
                return "No key combination provided."
            
            key_parts = [k.strip() for k in keys.split("+")]
            subprocess.run(["xdotool", "key"] + key_parts)
            return f"Successfully sent key combination: '{keys}'"

        elif action == "type_enter":
            if not text:
                return "No text provided to type."
            subprocess.run(["xdotool", "type", "--delay", str(int(delay*1000)), text])
            time.sleep(0.2)
            subprocess.run(["xdotool", "key", "Return"])
            return f"Successfully typed '{text}' and pressed Enter"

        else:
            return f"Unknown keyboard action: '{action}'"

    except Exception as e:
        return f"Error performing keyboard action: {e}"


def click_action(x: int, y: int, clicks: int = 1, button: str = "left"):
    """
    Click at specific coordinates.
    x, y: coordinates to click
    clicks: number of clicks (default 1)
    button: 'left', 'right', or 'middle' (default 'left')
    """
    try:
        if button.lower() == "right":
            pyautogui.rightClick(x, y, clicks=clicks)
        elif button.lower() == "middle":
            pyautogui.middleClick(x, y, clicks=clicks)
        else:
            pyautogui.click(x, y, clicks=clicks)
        
        return f"Successfully clicked at ({x}, {y}) with {button} button {clicks} time(s)"
    except Exception as e:
        return f"Error clicking: {e}"

def scroll_action(clicks: int, direction: str = "up"):
    """
    Scroll up or down.
    clicks: number of scroll steps
    direction: 'up' or 'down' (default 'up')
    """
    try:
        scroll_amount = clicks if direction.lower() == "up" else -clicks
        pyautogui.scroll(scroll_amount)
        return f"Successfully scrolled {direction} {clicks} times"
    except Exception as e:
        return f"Error scrolling: {e}"

def open_app(app_name: str):
    """
    Opens a known app on Ubuntu.
    app_name: friendly name (keys of KNOWN_APPS)
    """
    cmd = KNOWN_APPS.get(app_name.lower())
    if not cmd:
        return f"App '{app_name}' is not in the known apps list."

    try:
        subprocess.Popen([cmd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return f"Opening {app_name}..."
    except FileNotFoundError:
        return f"Could not open {app_name}. Command '{cmd}' not found."
    except Exception as e:
        return f"Error opening {app_name}: {e}"