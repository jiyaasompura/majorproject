from fastapi import FastAPI, UploadFile, HTTPException
from stt_module import transcribe_audio
from ai_module import get_ai_response
from tts_module import tts_speak

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Receptionist Backend is Running ✅"}

@app.post("/conversation/")
async def handle_call(audio: UploadFile):
    if not audio.filename.endswith((".mp3", ".wav")):
        raise HTTPException(status_code=400, detail="Unsupported audio format.")
    
    try:
        text = transcribe_audio(audio.file)
        ai_reply = get_ai_response(text)
        speech_path = tts_speak(ai_reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {
        "user_text": text,
        "ai_reply": ai_reply,
        "audio_path": speech_path
    }
