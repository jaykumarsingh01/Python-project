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


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)

    # if you want female voice then change index 0 to 1 :

    # engine.setProperty('voice',voices[1].id)    
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

# speechtx("hello Jay Kumar Singh and sonal singh son of vijay kumar singh and brother of varoon singh")


