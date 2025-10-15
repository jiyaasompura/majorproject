import requests
from pathlib import Path
import pygame  # for playback

API_KEY = "sk_fa943c2539f4e75f629f4e98aadd2a0f3bd202191b15dae4"
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # default male voice

def tts_speak(text):
    """Convert text to realistic voice using ElevenLabs API."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": API_KEY
    }
    data = {
        "text": text,
        "model_id": "eleven_turbo_v2",
        "voice_settings": {"stability": 0.3, "similarity_boost": 0.8}
    }

    # Send request
    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 200:
        raise Exception(f"TTS Error: {response.text}")

    # Save audio
    output_path = Path("response.mp3")
    with open(output_path, "wb") as f:
        f.write(response.content)

    # Play audio
    pygame.mixer.init()
    pygame.mixer.music.load(str(output_path))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
