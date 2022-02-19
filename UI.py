import  tkinter
from tkinter import *
import tkinter as tk
import pyttsx3
import speech_recognition as sr
import webbrowser
#text to speech conversion
def speaktext(text):
    friend=pyttsx3.init()
    friend.say(text)
    friend.runAndWait()
speaktext('Press Lets Chat Button to access Bot')
def getaudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speaktext('Im Listening')
        print('listening...')
        audio = r.listen(source)
        MyText = r.recognize_google(audio)
        return(MyText)
def speech():
    while True:
        query=getaudio().lower()
        if  'hello' in query :
            speaktext('Hi, How are you today')
        if  'i am Fine' in query:
            speaktext('Good')
        if 'bye' in query:
            speaktext('Bye')
        if 'open google' in query:
            speaktext('Redirecting to Google')
            webbrowser.open('https://www.google.ae')
        if 'open youtube music' in query:
            speaktext('Redirecting you to Youtube Music')
            webbrowser.open('https://www.youtube.com/watch?v=LrL8_b3LZLM')
        if 'open discord' in query:
            speaktext('Redirecting you to Discord')
            webbrowser.open('https://discord.com/channels/@me')
        if 'open twitter' in query:
            speaktext('Redirecting you to Twitter')
            webbrowser.open('https://twitter.com/home')
        if 'open Github' in query:
            speaktext('Redirecting you to Github')
            webbrowser.open('https://github.com/ItzSlayer09')
            #You can edit the ItzSlayer09 to you account or any of your Repositories.
def help():
    while True:
        query=getaudio().lower()
        if  'help' in query :
            speaktext('Please Press Lets Chat button and then When the Bot is Saying Im Listening then Speak if you want to stop the conversation then press the End button.')
            
from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
root = tk.Tk()
canvas = Canvas(root, width = 1630, height = 1080,bg='Dodger Blue')
canvas.pack()
img = ImageTk.PhotoImage(Image.open("D:\Saved Pictures\Robot.png"))
canvas.create_image(20, 50, anchor=NW, image=img)
btn1 = tk.Button(root, text = 'Lets Chat', bd = 10 ,command= speech, anchor='e',font=("comic sans",25,"bold",),bg='Green',fg='black',relief='raised')
canvas.create_window(800, 400, window=btn1)
btn2 = tk.Button(root, text = 'End', bd = 10,command = root.destroy ,anchor='e',font=("comic sans",25,"bold",),bg='red',fg='black',relief='raised')
canvas.create_window(800, 500, window=btn2)
btn3 = tk.Button(root, text = 'Help', bd = 10 ,command= help, anchor='e',font=("comic sans",25,"bold",),bg='Green',fg='black',relief='raised')
canvas.create_window(800, 600, window=btn3)
root.mainloop()

