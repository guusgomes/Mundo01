from random import randint

cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 28', '=' * 6, f'{cores['limpa']}')

numeropc = randint(0, 5)
numeropessoa = int(input('Pensei em um número de 0 a 5, que número é esse? '))

if numeropessoa == numeropc:
    print(f'Parabéns, você {cores['verde']}acertou{cores['limpa']}!')
else:
    print(f'Você {cores['vermelho']}errou{cores['limpa']}, eu pensei no número {cores['azul']}{numeropc}{cores['limpa']}!')