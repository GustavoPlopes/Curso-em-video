# Versão 1 playsound
# from playsound import playsound
# playsound('audio.mp3.mp3')

# Versão pygame
import pygame
pygame.init()
pygame.mixer.music.load('audio.mp3.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()