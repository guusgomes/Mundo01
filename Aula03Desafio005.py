cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 05', '=' * 6, f'{cores['limpa']}')

n = int(input('Digite um número inteiro: '))
sucessor = n + 1
antecessor = n - 1

print(f'Você digitou o número {cores['verde']}{n}{cores['limpa']}, seu antecessor é o {cores['amarelo']}{antecessor}{cores['limpa']} e seu sucessor é o {cores['azul']}{sucessor}{cores['limpa']}!')