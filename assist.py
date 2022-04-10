from ast import While
import pyttsx3

import speech_recognition as sr

import datetime

import pyaudio

import wikipedia

import webbrowser

import os

import smtplib

import googletrans


engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[-1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme(): #will greet you according to time of the day
    hour = int(datetime.datetime.now().hour)
    speak("hello sir .")    
    if hour>=0 and hour<12:         # if time is between 0 to 12 in the morning
        speak("Good Morning!")

    elif hour>=12 and hour<18:      #if time is between 12 to 6
        speak("Good Afternoon!")

    else:
         speak("Good Evining!")         
    speak("i am friday, how may i help you?")         

def listen():#it takes user input as audio of microphone and returns output as string variable 'query'


    k = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        k.pause_threshold == 1
        audio=k.listen(source)

    try:
        print("Recognizing......")
        speak("Recognizing......")
        query=k.recognize_google(audio, language='mar-in')    
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        speak("Say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('amolbrand00@gmail.com','amol@1234#')
    server.sendmail('amolbrand00@gmail.com',to,content)
    server.close()    

if __name__ == "__main__":
  # speak("Hello Boss")
   wishme()
while query!="stop":#In below code say somthing what do you want to open or get activity from friday and say stop to end process
    query=str(input( "enter query"))#to manualy enter query
    query =listen().lower()#to enter query with speach
    if 'wikipedia' in query:
            try:
                speak('searching Wikipedia....')
                query= query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=1)
                speak("Acording To Wikipedia")
                speak(results)
            except Exception as e:
                print(e)
                speak("sorry boss ,i am not able get any appropriate result from wikipedia")
    #Commands on os modules
    elif 'play video' in query:
            music_dir= 'C:\\Users\\Amol\\Desktop'
            video = os.listdir(music_dir)
            print(video)
            os.startfile(os.path.join(music_dir,video[22]))
    elif 'stop music' in query:
            music_dir= 'C:\\Users\\Amol\\Desktop'
            songs = os.listdir(music_dir)
            print(songs)
            os.close(os.path.join(music_dir,songs[0,])) 
    elif 'moonknight one' in query:
        dir='C:\\Users\\Amol\\Desktop\\moonknight'
        list=os.listdir(dir)
        print(list)
        os.startfile(os.path.join(dir,list[0]))
    elif 'moonknight two' in query:
        dir='C:\\Users\\Amol\\Desktop\\moonknight'
        list=os.listdir(dir)
        print(list)
        os.startfile(os.path.join(dir,list[1]))
    elif 'open file manager' in query:
            v='C:\\'
            os.startfile(v)      
    elif 'I want to watch movies' in query:
        dir='C:\\Users\\Amol\\Desktop\\movies'
        list=os.listdir(dir)
        print(list)

        

    # os.startfile(os.path.join(dir,list[]))

    # elif 'time' in query:
    #         strtime= datetime.datetime.now().strftime("%H:%M:%S")
    #         print(strtime)
    #         speak(f"The time is {strtime}")

    # elif 'email' in query:
    #         try:
    #             speak("what shoould I say?")
    #             content= listen()
    #             to= "amolbran0@gmail.com"
    #             sendEmail(to,content)
    #             speak("Email successfully send!")
    #         except Exception as e:
    #             print(e)
    #             speak("sorry boss, i am not able to send email")
    # elif 'open youtube' in query:
    #            webbrowser.open('https://youtu.be/iik25wqIuFo')

    # elif 'file' in query:
    #         v='C:\\'
    #         os.startfile(v)      

    elif'who are you' in query:
            speak('I am veronica, i am A.i system of created by self,with love of you, i m a ho,such a disspointment to this dammed world')
                
                          
   
