import speech_recognition as sr
import openai
import wikipedia
import os
import webbrowser
import pyttsx3
import musicLib
import link


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
        print(c)
        if(c.lower().startswith("open")):
            linked=c.lower().split(" ")[1]
            links=link.hyperlinks[linked]
            webbrowser.open(links)
            z=z+1
        elif(c.lower().startswith("play")):
            song = c.lower().split(" ")[1]
            link2= musicLib.music[song]
            webbrowser.open(link2)
            z=z+1

    

if __name__ == "__main__":
    speak("Initializing blackbird..........")
    while True:
    
        r = sr.Recognizer()
        
        print("recognizing........")
        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio=r.listen(source , timeout=4 , phrase_time_limit=2)
            word= r.recognize_google(audio)
            if(word.lower() == "blackbird","black bird","blackboard"):
                
                with sr.Microphone() as source:
                    speak("Blackbird activated......")
                    audio=r.listen(source,timeout=4 , phrase_time_limit=2)
                    command= r.recognize_google(audio)
                    processcommand(command)



        except Exception as e:
            print("can't understand speak again ; {0}".format(e))