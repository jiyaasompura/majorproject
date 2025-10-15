import sounddevice as sd
import numpy as np
import whisper
from ai_module import get_ai_response

# 1️⃣ Record audio
duration = 5  # seconds
fs = 16000
print("Recording...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
sd.wait()
print("Recording complete!")

# 2️⃣ Convert to 1D array for Whisper
audio = audio.flatten()

# 3️⃣ Load Whisper model
model = whisper.load_model("base")

# 4️⃣ Transcribe audio
result = model.transcribe(audio, fp16=False)
user_text = result['text']
print("User said:", user_text)

# 5️⃣ Get AI response
ai_reply = get_ai_response(user_text)
print("AI Response:", ai_reply)
