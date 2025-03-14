cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 30', '=' * 6, f'{cores['limpa']}')

n = int(input('Digite um número inteiro: '))

if n % 2 == 0:
    print(f'O número {n} é {cores['azul']}PAR{cores['limpa']}.')
else:
    print(f'O número {n} é {cores['amarelo']}ÍMPAR{cores['limpa']}.')