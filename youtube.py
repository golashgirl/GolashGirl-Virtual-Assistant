import pytube
import pyttsx3 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
video_url = 'https://www.youtube.com/watch?v=V7LwfY5U5WI'   
youtube = pytube.YouTube(video_url)  
video = youtube.streams.first()  
video.download('E:\\YOUTUBE TESTING')   
print("DOWNLOADING")
speak("Downloaded in YOUTUBE TESTING folder for you mam, Thankyou for using MALGO service")