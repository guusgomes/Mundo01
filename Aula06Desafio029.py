cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 29', '=' * 6, f'{cores['limpa']}')

velocidade = int(input('Digite a velocidade: '))

if velocidade >= 80.0:
    multa = (velocidade - 80) * 7
    print(f'{cores['amarelo']}Você excedeu o limite de 80km/h e foi multado em {cores['vermelho']}R$ {multa:.2f}{cores['limpa']}.')
print('Tenha um bom dia e lembre-se: Dirija com segurança!')