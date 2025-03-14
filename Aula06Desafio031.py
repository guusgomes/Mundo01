cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 31', '=' * 6, f'{cores['limpa']}')

distancia = float(input('Qual a distância da viagem? '))

if distancia <= 200.00:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

print(f'O valor da passagem para {cores['verde']}{distancia:.2f}km{cores['limpa']} é: {cores['amarelo']}R$ {valor:.2f}{cores['limpa']}.')