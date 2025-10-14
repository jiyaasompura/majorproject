import whisper

_model = None

def get_model():
    global _model
    if _model is None:
        _model = whisper.load_model("base")
    return _model

def transcribe_audio(audio_file):
    model = get_model()
    result = model.transcribe(audio_file, fp16=False)  # CPU safe
    return result['text']
