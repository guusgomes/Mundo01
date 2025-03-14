from math import radians, sin, cos, tan

cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 18', '=' * 6, f'{cores['limpa']}')

n = int(input('Digite o valor de um ângulo: '))
seno = sin(radians(n))
cosseno = cos(radians(n))
tangente = tan(radians(n))

print(f'Você digitou {cores['verde']}{n}º{cores['limpa']}, o {cores['amarelo']}seno{cores['limpa']} é {cores['amarelo']}{seno:.2f}{cores['limpa']}, o {cores['azul']}cosseno{cores['limpa']} é {cores['azul']}{cosseno:.2f}{cores['limpa']} e a {cores['magenta']}tangente{cores['limpa']} é {cores['magenta']}{tangente:.2f}{cores['limpa']}.')