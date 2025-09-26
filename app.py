import ollama
import json
from datetime import datetime
from actions import open_app  # your offline app executor
import requests
import tempfile
import os
import pygame
from murf import Murf

MODEL_NAME = "Ivy"
LOG_FILE = "ivy_outputs.json"

# Initialize Murf client
murf_client = Murf(api_key="ap2_686f974a-49a7-41d5-a227-4bedb5301505")
MURF_VOICE_ID = "en-US-Alicia"  # Natural female voice

def speak_murf(text: str):
    """Generate speech using Murf and play it."""
    # Generate TTS via Murf
    res = murf_client.text_to_speech.generate(text=text, voice_id=MURF_VOICE_ID)
    audio_url = res.audio_file

    # Download the audio
    response = requests.get(audio_url)
    response.raise_for_status()

    # Save to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(response.content)
        tmp_path = tmp.name

    # Play using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(tmp_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

    # Cleanup
    os.remove(tmp_path)

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
            print(f"\nIvy executed open_app: {result_msg}\n")
        else:
            print("\nNo app_name provided for open_app.\n")

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

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        result = query_ivy(user_input)
        print(f"\nIvy: {json.dumps(result, indent=2)}\n")
