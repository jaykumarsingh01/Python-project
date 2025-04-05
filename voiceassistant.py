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
            return data
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

if __name__ == '__main__':

#    if sptext().lower() == " hey sonal ":
        data1= sptext().lower()
        if "your name" in data1:
             name= "my name is sonal singh"
             speechtx(name)
        elif "how old are you" in data1:
             age ="i am 100 years old"
             speechtx(age)
        elif 'now time' in data1:
             time= datetime.datetime.now().strftime("%I%M%p")
             speechtx(time)
#    else:
#            print("thanks")




    
