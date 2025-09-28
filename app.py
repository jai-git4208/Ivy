import ollama
import json
from datetime import datetime
from actions import open_app, keyboard_action  # your offline app executor and keyboard function
import requests
import tempfile
import os
import pygame
from murf import Murf
from speech_utils import listen  # import your speech recognition function

MODEL_NAME = "Ivy"
LOG_FILE = "ivy_outputs.json"

# Initialize Murf client
murf_client = Murf(api_key="ap2_686f974a-49a7-41d5-a227-4bedb5301505")
MURF_VOICE_ID = "en-US-Alicia"  # Natural female voice

def log(message: str, code: int = 200):
    """Print Ivy logs with timestamp and code."""
    now = datetime.now().strftime("%H:%M:%S")
    print(f"Ivy: :{now}: {message} -- code({code})")

def speak_murf(text: str):
    """Generate speech using Murf and play it."""
    try:
        res = murf_client.text_to_speech.generate(text=text, voice_id=MURF_VOICE_ID)
        audio_url = res.audio_file
        response = requests.get(audio_url)
        response.raise_for_status()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(response.content)
            tmp_path = tmp.name

        pygame.mixer.init()
        pygame.mixer.music.load(tmp_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

        os.remove(tmp_path)
        log("TTS played successfully.", 200)
    except Exception as e:
        log(f"TTS error: {e}", 500)

def clean_output(raw_output: str) -> str:
    """Remove ```json and ``` wrappers if present, leaving pure JSON."""
    text = raw_output.strip()
    if text.startswith("```json"):
        text = text[len("```json"):].strip()
    if text.startswith("```"):
        text = text[3:].strip()
    if text.endswith("```"):
        text = text[:-3].strip()
    return text

def query_ivy(prompt: str):
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )

        raw_output = response["message"]["content"].strip()
        cleaned_output = clean_output(raw_output)

        try:
            parsed = json.loads(cleaned_output)
        except json.JSONDecodeError:
            parsed = {"action": "none", "params": {}, "response": cleaned_output}

        # Execute open_app if requested
        if parsed.get("action") == "open_app":
            app_name = parsed.get("params", {}).get("app_name")
            if app_name:
                result_msg = open_app(app_name)
                log(f"Executed open_app: {result_msg}", 200)
            else:
                log("No app_name provided for open_app.", 404)

        # Execute keyboard action if requested
        if parsed.get("action") == "type":
            params = parsed.get("params", {})
            text = params.get("text", "")
            keys = params.get("keys", "")
            delay = params.get("delay", 0.1)
            keyboard_type = params.get("type", "type")  # type, keys, or type_enter
            
            if keyboard_type == "type" and text:
                result_msg = keyboard_action("type", text=text, delay=delay)
            elif keyboard_type == "keys" and keys:
                result_msg = keyboard_action("keys", keys=keys)
            elif keyboard_type == "type_enter" and text:
                result_msg = keyboard_action("type_enter", text=text, delay=delay)
            else:
                result_msg = "Invalid keyboard action parameters."
            
            log(f"Executed keyboard action: {result_msg}", 200)

        # Save latest output
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "output": parsed
        }
        with open(LOG_FILE, "w") as f:
            json.dump(log_entry, f, indent=2)

        # Speak Ivy's response
        if "response" in parsed:
            speak_murf(parsed["response"])

        return parsed
    except Exception as e:
        log(f"Error querying Ivy: {e}", 500)
        return {"action": "none", "params": {}, "response": "Error occurred."}

if __name__ == "__main__":
    log("Ivy started. Say 'quit' or 'exit' to stop.", 200)
    while True:
        user_input = listen()  # <-- use mic input now
        if user_input.lower() in ["quit", "exit"]:
            log("Exiting Ivy.", 200)
            break
        if user_input.strip() == "":
            log("No input detected.", 404)
            continue
        result = query_ivy(user_input)
        log(f"Response: {result.get('response', '')}", 200)