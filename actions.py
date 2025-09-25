import subprocess

# Dictionary of known apps with their command names
KNOWN_APPS = {
    "chrome": "google-chrome",
    "firefox": "firefox",
    "vscode": "code",
    "file_manager": "nautilus",
    "terminal": "gnome-terminal",
    "spotify": "spotify"
}

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
if __name__ == "__main__":
    while True:
        app = input("Which app do you want to open? ")
        if app.lower() in ["quit", "exit"]:
            break
        print(open_app(app))
