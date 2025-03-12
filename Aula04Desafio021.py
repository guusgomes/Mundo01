import pygame
print('='*6,'DESAFIO 21','='*6)
pygame.mixer.init()
pygame.mixer.music.load('nokia.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()