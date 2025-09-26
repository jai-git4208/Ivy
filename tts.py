import requests
import tempfile
import os
import pygame
from murf import Murf

# Init Murf client
client = Murf(api_key="ap2_686f974a-49a7-41d5-a227-4bedb5301505")

# Generate speech
res = client.text_to_speech.generate(
    text="Hello, I'm Ivy. Your smart AI assistant. How can I help you today?",
    voice_id="en-US-Alicia",
)

# Get Murf's audio URL
audio_url = res.audio_file

# Download the audio file
response = requests.get(audio_url)
response.raise_for_status()

# Save to a temporary file
with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
    tmp.write(response.content)
    tmp_path = tmp.name

# Play using pygame (cross-platform)
pygame.mixer.init()
pygame.mixer.music.load(tmp_path)
pygame.mixer.music.play()

# Wait until it finishes
while pygame.mixer.music.get_busy():
    continue

# Cleanup
os.remove(tmp_path)
