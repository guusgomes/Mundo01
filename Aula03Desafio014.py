cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 14', '=' * 6, f'{cores['limpa']}')

c = float(input('Qual a temperatura em °C? '))
f = (c * 9 / 5) + 32

print(f'A temperatura {cores['azul']}{c}°C{cores['limpa']} equivale a {cores['verde']}{f}°F{cores['limpa']}!')