from tkinter import *
import speech_recognition as sr                        #namespacing or aliasing
import pyttsx3
from datetime import datetime

root = Tk()                         #root is an object for Tk() class(Creates the Tkinter window)
root.geometry("500x500")

tts = pyttsx3.init()

def speak(audio):
    tts.say(audio)
    tts.runAndWait()
    
def r_audio():
    speak("How can I help you")
    speech_rec = sr.Recognizer()   # sr is the library, Recognizer() is a class, speech_rec is the object we created for the class
    with sr.Microphone() as source:          # With block makes sure that a resourse is released automatically once the block ends 
        audio = speech_rec.listen(source)           # Whatever the microphone listens, the function listen() stores that in the audio variable
        voice_data=''
        try:
            voice_data = speech_rec.recognize_google(audio, language = 'en-in')     # It converts speech(stored in audio variable) to text of a specific language format
        except sr.UnknownValueError:
            print("Can you Please repeat, I didn't get that? 👂")
            speak("Can you Please repeat, I didn't get that?")
            
    respond(voice_data)
    
def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        speak("My name is Junior Vihaan")
        print("My name is Jr.Vihaan")
    if "time" in voice_data:
        speak('Current Time is')
        now = datetime.now()
        ct = now.strftime("%H:%M:%S")
        speak(ct)
        print(ct)
    if "video game" in voice_data:
        speak("My Favourite video games include Brawl Stars, Clash Royal and GT sport")
        print("My Favourite video games include Brawl Stars, Clash Royal and GT sport")
    if(('old' in voice_data) or ('age' in voice_data)):
        speak("My age is 11 as of now")
        print("My age is 11 as of now")
    
r_audio()
root.mainloop()
            
        