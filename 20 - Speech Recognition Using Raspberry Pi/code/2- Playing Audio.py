import pygame
#initialize the mixer module
pygame.mixer.init()
#Load a music file for playback
pygame.mixer.music.load("../Records/date.mp3") # can be .wav
#Start the playback of the music stream
pygame.mixer.music.play()
