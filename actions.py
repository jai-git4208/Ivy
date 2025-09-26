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
    Performs keyboard actions using pyautogui.
    action: 'type', 'keys', or 'type_enter'
    text: text to type (for 'type' and 'type_enter' actions)
    keys: key combination (for 'keys' action, e.g., 'ctrl+c', 'alt+tab', 'f5')
    delay: delay between characters in seconds for typing (default 0.1)
    wait_time: delay before executing action in seconds (default 0 - no delay)
    """
    try:
        if action == "type":
            if not text:
                return "No text provided to type."
            
            # Optional wait time
            if wait_time > 0:
                print(f"Typing '{text}' in {wait_time} seconds...")
                time.sleep(wait_time)
            
            # Type the text with specified delay
            pyautogui.typewrite(text, interval=delay)
            
            return f"Successfully typed: '{text}'"
            
        elif action == "keys":
            if not keys:
                return "No key combination provided."
            
            # Optional wait time
            if wait_time > 0:
                print(f"Sending key combination '{keys}' in {wait_time} seconds...")
                time.sleep(wait_time)
            
            # Handle key combinations
            if '+' in keys:
                # Split combination like 'ctrl+c' or 'alt+tab'
                key_parts = [k.strip().lower() for k in keys.split('+')]
                
                # Map common key names to pyautogui format
                key_mapping = {
                    'ctrl': 'ctrl',
                    'alt': 'alt',
                    'shift': 'shift',
                    'super': 'win',  # Windows/Super key
                    'super_l': 'winleft',
                    'super_r': 'winright',
                    'tab': 'tab',
                    'return': 'enter',
                    'enter': 'enter',
                    'escape': 'esc',
                    'print': 'printscreen',
                    'f1': 'f1', 'f2': 'f2', 'f3': 'f3', 'f4': 'f4',
                    'f5': 'f5', 'f6': 'f6', 'f7': 'f7', 'f8': 'f8',
                    'f9': 'f9', 'f10': 'f10', 'f11': 'f11', 'f12': 'f12'
                }
                
                # Convert keys to pyautogui format
                converted_keys = []
                for key in key_parts:
                    converted_keys.append(key_mapping.get(key, key))
                
                # Execute hotkey combination
                pyautogui.hotkey(*converted_keys)
                
            else:
                # Single key press
                key_mapping = {
                    'return': 'enter',
                    'escape': 'esc',
                    'print': 'printscreen',
                    'super_l': 'winleft',
                    'super_r': 'winright'
                }
                
                mapped_key = key_mapping.get(keys.lower(), keys.lower())
                pyautogui.press(mapped_key)
            
            return f"Successfully sent key combination: '{keys}'"
            
        elif action == "type_enter":
            if not text:
                return "No text provided to type."
            
            # Type text first
            type_result = keyboard_action("type", text=text, delay=delay, wait_time=wait_time)
            if "Successfully typed" in type_result:
                time.sleep(0.2)  # Small pause before Enter
                enter_result = keyboard_action("keys", keys="enter")
                return f"{type_result}\n{enter_result}"
            return type_result
            
        else:
            return f"Unknown keyboard action: '{action}'. Use 'type', 'keys', or 'type_enter'."
            
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


    
# Example usage

