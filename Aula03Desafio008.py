cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 08', '=' * 6, f'{cores['limpa']}')

metros = float(input('Digite o valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000

print(f'{cores['verde']}{metros}{cores['limpa']} metros é igual a {cores['vermelho']}{centimetros}{cores['limpa']} centímetros e {cores['amarelo']}{milimetros}{cores['limpa']} milímetros!')