
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():

    try:
        with sr.Microphone() as source:
            print("say.....")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "alexa" in command:
                command=command.replace('alexa','')
                
                print(command)
    except:
        print("say again")
    return command

def run_alexa():
    command=take_command()
    if "play" in command:
        song=command.replace('play',' ')
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time=datetime.datetime.now().strftime('%H:%M:%S')
        talk("current time is" + time)
        print(time)
    elif "tell me about" in command:
        person=command.replace('tell me about','')
        info=wikipedia.summary(person,10)
        print(info)
        talk(info)
    elif 'date'  in command:
        
        talk("i have a boyfriend")
    elif "are you in relationship" in command:
        talk("i am in a relationship with wifi sorry")
    else:
        talk("please say command again.i didn't understand")

while True:

 run_alexa()
