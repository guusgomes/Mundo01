cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 03', '=' * 6, f'{cores['limpa']}')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
soma = n1 + n2

print(f'A soma é {cores['verde']}{soma}{cores['limpa']}.')