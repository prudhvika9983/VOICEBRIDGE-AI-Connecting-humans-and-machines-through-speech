import speech_recognition as sr

def transcribe_audio_file(audio_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            # Optimized for Indian accent
            text = recognizer.recognize_google(audio_data, language="en-IN")
            return text
    except Exception as e:
        print(f"STT Error: {e}")
        return None