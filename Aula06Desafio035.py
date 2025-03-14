cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 35', '=' * 6, f'{cores['limpa']}')

r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite outro comprimento: '))
r3 = float(input('Digite o último comprimento: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'As retas digitadas {cores['verde']}FORMAM{cores['limpa']} um triângulo!')
else:
    print(f'As retas digitadas {cores['vermelho']}NÃO FORMAM{cores['limpa']} um triângulo!')