import pygame

cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 21', '=' * 6, f'{cores['limpa']}')

pygame.mixer.init()
pygame.mixer.music.load('nokia.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()