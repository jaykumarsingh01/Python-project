import pyttsx3 # type: ignore
import speech_recognition as sr # type: ignore
import webbrowser
import datetime
import pyjokes # type: ignore

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")
            data = recognizer.recognize_sphinx(audio)
            print(data)
        except sr.UnknownValueError:
            print("not understanding")

sptext()