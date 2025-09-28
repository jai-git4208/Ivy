import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    # Adjust these values to be more sensitive to silence
    r.energy_threshold = 900  # Higher = less sensitive to quiet sounds
    r.dynamic_energy_threshold = False  # Don't auto-adjust
    r.pause_threshold = 4  # Seconds of silence before considering phrase complete
    
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        
        try:
            # timeout: stop listening if no speech starts within X seconds
            # phrase_time_limit: stop recording after X seconds of speech
            audio = r.listen(source, timeout=2, phrase_time_limit=3)
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""
    
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError as e:
        print(f"API error: {e}")
        return ""