cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 10', '=' * 6, f'{cores['limpa']}')

reais = float(input('Quantos reais você tem? '))
dolares = reais / 3.27

print(f'Com {cores['verde']}R$ {reais:.2f}{cores['limpa']}, você pode comprar {cores['azul']}U$ {dolares:.2f}{cores['limpa']}!')