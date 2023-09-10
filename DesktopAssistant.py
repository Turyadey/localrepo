# NIX AI DEMO(Personal Desktop Assistant)

import pyttsx3
import datetime
import speech_recognition as sr  
import wikipedia           
import webbrowser        
import os  
import random
import smtplib  
import pywhatkit as kit  
import cv2  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
# define engine for voices

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate',170)

# define speak function
# this function will program your Nix to speak something

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Define wishMe function
# this function will make your Nix wish you according to system time 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good Morning!")
    elif hour>= 12 and hour<18:
        Speak("Good Afternoon!")
    else:
        Speak("Good Evening!")

    Speak("Hello sir. How can I help you?")

# Define takeCommand function
# this function will make your Nix to take microphone input from the user and return a string output

def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")  
    except Exception as e:
        print(e)
        print("Say that again please...")     
        return "None"
    return query   

# define sendEnail function
# this function will make your Nix to send emails as per your concern
  
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_gmailid', 'your password-here')
    server.sendmail('turyadey13@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

# Logic for executing tasks based on query

        if 'wikipedia' in query:
            Speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences= 7)
            Speak("According to Wikipedia")
            print(results)
            Speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            Speak('What should i search on google?')
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'send message' in query:
            kit.sendwhatmsg("+919832718102","this is a testing protocol", 2,25)

        elif 'play music' in query:
            music_dir = 'D:\\songs'  
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            Speak(f"Sir, the time is {strTime}") 

        elif 'open code' in query:
            codePath = "C:\\Users\\TURYA DEY\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"  
            os.startfile(codePath)   


        elif 'send email' in query:
            try:
                Speak("What should I say?")
                content = takeCommand()
                to = "turyadey13@gmail.com"
                sendEmail(to,content)
                Speak("Email has been sent")
            except Exception as e:
                print(e)
                Speak("Sorry my friend. I am not able to send this email")

        elif 'open command prompt' in query:
            os.system('start cmd')   

        elif 'open webcam' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, video_data = cap.read()
                cv2.imshow('webcam', video_data)
                if cv2.waitKey(10) == ord('a'):
                    break
            cap.release()   
