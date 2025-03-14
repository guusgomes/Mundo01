cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 06', '=' * 6, f'{cores['limpa']}')

n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print(f'Você digitou o número {cores['verde']}{n}{cores['limpa']}, seu dobro é {cores['vermelho']}{dobro}{cores['limpa']}, seu triplo é {cores['amarelo']}{triplo}{cores['limpa']} e sua raiz quadrada é {cores['azul']}{raiz}{cores['limpa']}!')