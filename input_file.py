'''
for text input
def takes_input():
    i = input("You: ")
    return i
'''

import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5') #sapi5 is microsoft speech api (Speech Application Programming Interface)
voices = engine.getProperty("voices")
engine. setProperty('voices', voices[0].id) #0 is male(david) and 1 is female(zira)



# greets and asks the user what to do
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r = sr.Recognizer() # recognizer class helps to recognise audio
    with sr.Microphone() as source:
        speak("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        i = r.recognize_google(audio, language= "en-in")
        print(f"You: {i}\n")

    except Exception as e:
        # print(e)  #to print error
        speak("Say that again please...")
        takeCommand()

    return i
