cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 15', '=' * 6, f'{cores['limpa']}')

km = float(input('Quantos KMs percorreu? '))
dias = int(input('Por quantos dias utilizou? '))
valor = (km * 0.15) + (dias * 60)

print(f'O valor total para {cores['azul']}{km}km{cores['limpa']} e {cores['verde']}{dias} dias{cores['limpa']} é de: {cores['magenta']}R$ {valor:.2f}{cores['limpa']}!')