import pyttsx3
import speech_recognition as sr
import datetime
import os
import sys
import wikipedia
import pywhatkit
import pyautogui
import pyjokes

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=2
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
        
    try:
        print('wait for few moments.........')
        query=r.recognize_google(audio,language='en-in')
        print(f"You just said : {query}\n")
    except Exception as e:
        print(e)
        speak("Please tell me again")
        query="none"
    return query

def wishings():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Master")
        speak("Good Morning Master")
    elif hour>=12 and hour<17:
        print("Good Afternoon Master")
        speak("Good Afternoon Master")
    elif hour>=17 and hour<21:
        print("Good Evening Master")
        speak("Good Evening Master")
    else:
        print("Good Night Master")
        speak("Good Night Master")
    
if __name__=="__main__":
    wishings()
    query=commands().lower()
    if 'time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Master,the time is {strTime}")
    
    elif 'open browser' in query:
        speak("Opening Browser Master.....")
        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
        
    elif 'wikipedia' in query:
        speak("Searching in Wikipedia.....")
        try:
            query=query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia,")
            print(results)
            speak(results)
        except:
            speak("No results found....")
            print("No results found....")
    
    elif 'play' in query:
        query=query.replace('play', '')
        speak('Playing '+query)
        print("playing "+query)
        pywhatkit.playonyt(query)
        
    elif 'type' in query:
        speak("Please tell me what should i write...")
        while True:
            writeInNotepad=commands()
            if writeInNotepad=='exit typing':
                speak("Done sir")
                break
            else:
                pyautogui.write(writeInNotepad)
                
    elif 'joke' in query:
        joke=pyjokes.get_joke()
        print(joke)
        speak(joke)
    
    elif 'exit program' in query:
        speak("I'm Leaving sir, bye!")
        sys.exit()
        