'''print('='*10,'DESAFIO 33','='*10)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite o último número: '))

if n1 > n2 and n1 > n3 and n2 > n3:
    maior = n1
    menor = n3
elif n1 > n2 and n1 > n3 and n3 > n2:
    maior = n1
    menor = n2
elif n2 > n1 and n2 > n3 and n1 > n3:
    maior = n2
    menor = n3
elif n2 > n1 and n2 > n3 and n3 > n1:
    maior = n2
    menor = n1
elif n3 > n1 and n3 > n2 and n1 > n2:
    maior = n3
    menor = n2
else:
    maior = n3
    menor = n1

print(f'O maior número digitado é {maior} e o menor {menor}.')'''

cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 33', '=' * 6, f'{cores['limpa']}')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite o último número: '))
menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

maior = n1
    
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

print(f'O {cores['azul']}maior{cores['limpa']} número digitado é {cores['azul']}{maior}{cores['limpa']} e o {cores['amarelo']}menor{cores['limpa']} é {cores['amarelo']}{menor}{cores['limpa']}.')