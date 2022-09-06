# data from other files
from tkinter.constants import GROOVE, RIDGE
from input_file import takeCommand
from process_file import executes_process
import datetime #date time module
import pyttsx3 # make the computer speak
import speech_recognition as sr # take audio command from user
import tkinter 
import os
os.system("cls") #to run cmd commands


engine = pyttsx3.init('sapi5') #sapi5 is microsoft speech api (Speech Application Programming Interface)
voices = engine.getProperty("voices")
engine.setProperty('voices', voices[1].id) #0 is male(david) and 1 is female(zira)

print("time; date; joke; notepad; spotify; search internet:google, google scholar,youtube, wikipedia, temperature")

# greets and asks the user what to do
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")
            
    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("How may I help you today?")

class Khidki:

    def __init__(self) -> None:
        root = tkinter.Tk()

        root.geometry("200x200")
        root.title("Mitra")

        userText=tkinter.StringVar()
        MitraText=tkinter.StringVar()

        userText.set("User: ")
        MitraText.set("Starting Mitra")

        f1 = tkinter.LabelFrame(root, text="User: ", borderwidth=5, relief=GROOVE)

        userMsg =tkinter.Message(f1, text=userText.get(), bg="#e7f5fe", fg= "black", font="ariel 10", padx="5", pady="20", borderwidth=5, relief=RIDGE).pack(fill="both")

        f1.pack(side="top", fill="both",expand="yes")

        f2 = tkinter.LabelFrame(root, text="Mitra: ", borderwidth=5, relief=GROOVE)

        MitraMsg =tkinter.Message(f2, text=MitraText.get(), bg="#e7f5fe", fg= "black", font="ariel 10", padx="5", pady="20", borderwidth=5, relief=RIDGE).pack(fill="both")

        f2.pack(side="top", fill="both",expand="yes")

        b1 = tkinter.Button(root, text="Close!", bg="grey", fg="white", font="ariel 8", command=root.destroy).pack(fill="x")

        root.mainloop()

    def clicked(self, query):
        query=takeCommand()
        self.userText.set("Listening...")
        self.userText.set(query)


if __name__=="__main__":
    wishMe()
    khidki=Khidki()
    


if 1: #to keep the assistant working
    i = takeCommand() # takes input
    q = executes_process(i.lower())


    