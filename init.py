import speech_recognition as sr
import pyttsx3

#Videoclip Ulises https://www.youtube.com/watch?v=-kb5VIV8zIk

def talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    listener = sr.Recognizer()
    name = "yarbiss"
    engine = pyttsx3.init()

    voices = engine .getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    try:
        with sr.Microphone() as source:
            print("Estoy escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language = 'es-ES')
            if name in rec.lower():
                talk("no me sale de los cojones")
            print(rec)
    except Exception as e:
        print(e)
        pass