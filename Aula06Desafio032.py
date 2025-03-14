'''print('='*10,'DESAFIO 32','='*10)

ano = int(input('Digite um ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')'''

from datetime import date

cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 26', '=' * 6, f'{cores['limpa']}')

ano = int(input(f'Digite um ano {cores['amarelo']}(0 para o ano atual){cores['limpa']}: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} {cores['verde']}é bissexto{cores['limpa']}.')
else:
    print(f'O ano {ano} {cores['vermelho']}não é bissexto{cores['limpa']}.')