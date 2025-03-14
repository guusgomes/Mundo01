cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 09', '=' * 6, f'{cores['limpa']}')

n = int(input('Digite um número inteiro: '))

print(f'A tabuada do número {cores['vermelho']}{n}{cores['limpa']} é:')
print(f'{cores['amarelo']}{n} X 01{cores['limpa']} = {cores['vermelho']}{n * 1}{cores['limpa']}')
print(f'{cores['amarelo']}{n} X 02{cores['limpa']} = {cores['vermelho']}{n * 2}{cores['limpa']}')
print(f'{cores['amarelo']}{n} X 03{cores['limpa']} = {cores['vermelho']}{n * 3}{cores['limpa']}')
print(f'{cores['amarelo']}{n} X 04{cores['limpa']} = {cores['vermelho']}{n * 4}{cores['limpa']}')
print(f'{cores['amarelo']}{n} X 05{cores['limpa']} = {cores['vermelho']}{n * 5}{cores['limpa']}')
print(f'{cores['amarelo']}{n} X 06{cores['limpa']} = {cores['vermelho']}{n * 6}{cores['limpa']}')
print(f'{cores['amarelo']}{n} X 07{cores['limpa']} = {cores['vermelho']}{n * 7}{cores['limpa']}')
print(f'{cores['amarelo']}{n} X 08{cores['limpa']} = {cores['vermelho']}{n * 8}{cores['limpa']}')
print(f'{cores['amarelo']}{n} X 09{cores['limpa']} = {cores['vermelho']}{n * 9}{cores['limpa']}')
print(f'{cores['amarelo']}{n} X 10{cores['limpa']} = {cores['vermelho']}{n * 10}{cores['limpa']}')