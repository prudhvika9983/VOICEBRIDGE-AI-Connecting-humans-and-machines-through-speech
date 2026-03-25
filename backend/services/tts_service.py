import os
from google.cloud import texttospeech
from dotenv import load_dotenv

load_dotenv()

def generate_voice(text):
    try:
        # Standard Google TTS client
        client = texttospeech.TextToSpeechClient()
        
        input_text = texttospeech.SynthesisInput(text=text)

        # Note: 'en-IN-Wavenet-D' is a very high-quality Indian English voice
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-IN",
            name="en-IN-Wavenet-D"
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = client.synthesize_speech(
            request={"input": input_text, "voice": voice, "audio_config": audio_config}
        )

        # Save to a temporary file for the frontend to play
        file_path = "static/response.mp3"
        with open(file_path, "wb") as out:
            out.write(response.audio_content)
        
        return f"http://127.0.0.1:8000/{file_path}"
    except Exception as e:
        print(f"TTS Error: {e}")
        return None