cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 26', '=' * 6, f'{cores['limpa']}')

nome = str(input('Digite seu nome completo: ')).strip().split()

print(f'Primero nome: {cores['verde']}{nome[0]}{cores['limpa']}.')
print(f'Último nome: {cores['azul']}{nome[len(nome) - 1]}{cores['limpa']}.')