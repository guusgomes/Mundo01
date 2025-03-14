from math import trunc
cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 11', '=' * 6, f'{cores['limpa']}')

n = float(input('Digite um número real qualquer: '))

print(f'O número {cores['azul']}{n}{cores['limpa']} tem a parte inteira {cores['verde']}{trunc(n)}{cores['limpa']}.')

##print('='*6,'DESAFIO 16','='*6)
##n = float(input('Digite um número real qualquer: '))
##print(f'O número {n} tem a parte inteira {int(n)}.')