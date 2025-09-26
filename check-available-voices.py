import pyttsx3
engine = pyttsx3.init()
for v in engine.getProperty("voices"):
    print(v.id, v.name)
