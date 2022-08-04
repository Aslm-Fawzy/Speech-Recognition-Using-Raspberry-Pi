#Importing  Packages
import speech_recognition as sr
from datetime import date
from gpiozero import LED
from time import sleep
from gtts import gTTS
import pygame


mytext = """
     hello sir ^_^
          For Knowing Date : say (today)
          For Turn on Led : say (open)
          For Turn off Led : say (close)
          For Closing Program : say (exit)
      """
print(mytext)


# Set Led to Connected Pin (21)
red = LED(21)


'''
Making Object from Recognizer Class that help us in :
   1- converting audio to text
   2- Detect if there is Silence or Audio (espically during using microphone)
'''

r = sr.Recognizer()


#Making Object from Microphone Class as our Input speech will be from microphone
mic = sr.Microphone()


while True:
    #Opening Microphone 
    with mic as source:
        #Capturing Audio and Assign it in Variable 
        audio = r.listen(source)
    #Recognize Captured Audio using Google Web Search API   
    words = r.recognize_google(audio)
    print(words)


    if words == "today":
        print(date.today())


    elif words == "open":
        red.on()       


    elif words == "close":
        red.off()
        
    elif words == "exit":
        print("...")
        print("...")
        print("...")
        print("Good Bye :)")
        break
