import subprocess
import pyttsx3 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
subprocess.Popen('explorer "D:\\imp doc\\ID.jpg"')
print("Done Mam")
speak("OPENING YOU COLLEGE ID")