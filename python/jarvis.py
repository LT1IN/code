import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
import os


jarvis=pyttsx3.init()
voices = jarvis.getProperty('voices')
jarvis.setProperty('voice', voices[0].id) 

def speak(audio):
    print('J.A.R.V.I.S: ' + audio)
    jarvis.say(audio)
    jarvis.runAndWait()

   
    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p") 
    speak("what time is it")
    speak(Time)

def welcome():
        #hello
        hour=datetime.datetime.now().hour
        if hour >= 6 and hour<12:
            speak("Good Morning Sir!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon Sir!")
        elif hour>=18 and hour<24:
            speak("Good Evening sir")
        speak("how can i help you") 


def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query = c.recognize_google(audio,language='en-US')
        print("LTT: "+query)
    except sr.UnknownValueError:
        speak("sorry i can't hear you please typing your order")
        query = str(input('Your order is: '))
    return query

if __name__  =="__main__":
    welcome()

    while True:
        query=command().lower()
        #All the command will store in lower case for easy recognition
        if "google" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        if "hi jarvis" in query:
            speak("hello Tin")
        if "hello" in query:
            speak("hello, what would you want today")
        elif "youtube" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')

        elif "goodnight jarvis" in query:
            speak("jarvis is off. Goodbye boss")
            quit()
        elif "open video" in query:
            meme =r"E:\meme\troll.mp4"
            os.startfile(meme)
        elif 'time' in query:
            time()

        