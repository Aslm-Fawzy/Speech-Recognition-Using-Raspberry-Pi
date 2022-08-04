#!/usr/bin/env python
# coding: utf-8

# # Full Project

# In[ ]:


#Importing  Packages
import speech_recognition as sr
from datetime import date
from gpiozero import LED
from time import sleep
from gtts import gTTS
import pygame


#initialize the mixer module
pygame.mixer.init()
#Load a music file for playback
pygame.mixer.music.load("../Records/welcome.mp3")
#Start the playback of the music stream
pygame.mixer.music.play()


mytext = """
     hello sir ^_^
          For Knowing Date : say (today)
          For Turn on Led : say (open)
          For Turn off Led : say (close)
          For Closing Program : say (exit)
      """
print(mytext)
# Pause Excute of Code for 15 Second untill Welcome Audio Ended
sleep(15)


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
        date_text = str(date.today())
        date_obj = gTTS(text=date_text, lang='en', slow=False)
        date_obj.save("../Records/date.mp3")
        pygame.mixer.music.load("../Records/date.mp3") 
        pygame.mixer.music.play()
# Pause Excute of Code for 3.5 Seconds untill Audio Ended        
        sleep(3.5)



    elif words == "open":
        red.on()
        pygame.mixer.music.load("../Records/open.mp3") 
        pygame.mixer.music.play()
# Pause Excute of Code for 3.5 Seconds untill Audio Ended                
        sleep(3.5)        




    elif words == "close":
        red.off()
        pygame.mixer.music.load("../Records/close.mp3") 
        pygame.mixer.music.play()
# Pause Excute of Code for 3.5 Seconds untill Audio Ended                
        sleep(3.5)


        
    elif words == "exit":
        print("...")
        print("...")
        print("...")
        print("Good Bye :)")
        pygame.mixer.music.load("../Records/exit.mp3") 
        pygame.mixer.music.play()
        break

