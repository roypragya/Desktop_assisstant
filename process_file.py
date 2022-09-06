from datetime import datetime
from input_file import speak, takeCommand
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
import pyjokes


engine = pyttsx3.init('sapi5') #sapi5 is microsoft speech api (Speech Application Programming Interface)
voices = engine.getProperty("voices")
engine. setProperty('voices', voices[0].id) #0 is male(david) and 1 is female(zira)


def executes_process(query):
    if "time" in query:
        current_time = datetime.now().strftime("%H hours %M Minutes")
        print(current_time)
        speak(current_time)

    elif "date" in query:
        current_time = datetime.now().strftime("%A, %x")
        print(current_time)
        speak(current_time)
        

    elif "google" in query:
        if "scholar" in query:
            speak("searching...")
            query = query.replace("google scholar", "")
            webbrowser.open(f"https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={query}")
        else:
            speak("searching internet...")
            query = query.replace("google", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "temperature" in query:
        query = query.replace("temperature","")
        data = requests.get(f"https://www.google.com/search?q=temperature%20today%20{query}") 
        result = BeautifulSoup(data.text, "html.parser")
        temp = result.find("div", class_="BNeawe").text
        speak(f"Temprature in {query} is {temp}")
    
    elif 'joke' in query:
        speak(pyjokes.get_joke())

    # elif "wi-fi" in query:
    #     # query= query.replace("wi-fi","")
    #     speak(os.system("netsh wlan show interfaces"))

    elif "youtube" in query or "videos" in query:
        speak("YouTube")
        query = query.replace("youtube","").replace("videos","").replace("video","")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    elif 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            speak('Searching Wikipedia...')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

    elif "Notepad" in query:
        speak("Opening Notepad...")
        os.system("notepad")

    elif "spotify" in query:
        speak("Opening Spotify...")
        os.system("Spotify")
    
    else:
        speak("kya tutul putul kiya....?")
        takeCommand()
        

    # return query

