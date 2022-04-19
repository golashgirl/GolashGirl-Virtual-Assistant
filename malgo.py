import os
import pyautogui as vidhi2
import pyttsx3 
import pywhatkit as vidhi
import speech_recognition as vidhi1
import wikipedia 
import webbrowser
import datetime
import cv2
import pytube  
from pytube import YouTube  
import numpy as np
import subprocess



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Mam, Have Your Tea Or Coffee!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Mam, Have Your Lunch or not!")   

    else:
        speak("Good Evening  Mam ,Have Your Snacks or not!")  

    speak("I am MALGO Your Personal Assistant Mam. How may I help you")       

def Command():

    r = vidhi1.Recognizer()
    with vidhi1.Microphone() as source:
       r.adjust_for_ambient_noise(source,duration=4)
       print("Listening You Mam......")
       speak("Listening You Mam......")
       r.pause_threshold = 0.6
       audio = r.listen(source)

    try:
        print("Trying to understand...")
        speak("Trying to understand...")    
        query = r.recognize_google(audio, language='en-in').lower()
        print("Ok Mam :-)\n")
        speak("Ok Mam \n")

    except Exception as e:
        
        print(e)
        print("Please Say That Again Mam...")
        speak("Please Say That Again Mam...")  
        return "None"
    return query


if __name__ == "__main__":
    greet()
    while (True):

        query = Command().lower()
       
        if 'tell me about ' in query:
            speak('Searching From Internet...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("As Internet Says...")
            print(results)
            speak(results)

        elif 'open my google' in query:
            webbrowser.open("www.google.com")
            print("Opening Google")
            speak("Opening Google")
            
        elif 'take screenshot'in query:
            SS = vidhi2.screenshot()
            SS.save("E:\\TEST\\pic1.png")
            print("Screenshot Saved")
            speak("Screenshot Saved")
            
        elif 'remove watermark' in query:
            img = cv2.imread("E:\\TEST1\\input.jpg")
            alpha = 2.0
            beta = -160
            new = alpha * img + beta
            new = np.clip(new, 0, 255).astype(np.uint8)
            cv2.imwrite("E:\\TEST1\\output.jpg", new)
            print("Watermark Removed For You Mam")
            speak("Watermark Removed For You Mam")
        
        elif 'youtube video' in query:
           
            video_url = 'https://www.youtube.com/watch?v=V7LwfY5U5WI'   
            youtube = pytube.YouTube(video_url)  
            video = youtube.streams.first()  
            video.download('E:\\FILMS')   
            print("DOWNLOADING")
            print("Video Saved")
            speak("Video Saved")
            
            
        elif 'send whatsapp to me' in query:
            vidhi.sendwhatmsg("+919520409828","Hi Mam how are you?",17,37)
            print("Sending Whatsapp Message")
            speak("Sending Whatsapp Message")
            
         
                          
        elif 'open my youtube' in query:
            webbrowser.open("www.youtube.com")
            print("Done Mam")
            speak("Done Mam")
            

        elif 'open my ID' in query:
            subprocess.Popen('explorer "D:\\TEST IMAGE\\ID.jpg"')
            print("Done Mam")
            speak("Done Mam")

        elif 'tell me the current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Mam, the time is {strTime}")

        