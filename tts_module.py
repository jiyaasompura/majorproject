import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_speech(text, output_file="response.mp3"):
    try:
        with openai.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=text
        ) as response:
            response.stream_to_file(output_file)
        return output_file
    except Exception as e:
        print("TTS Error:", e)
        return None
