cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 11', '=' * 6, f'{cores['limpa']}')

largura = float(input(f'Digite a {cores['vermelho']}largura{cores['limpa']} da parede em metros: '))
altura = float(input(f'Digite a {cores['vermelho']}altura{cores['limpa']} da parede em metros: '))
area = largura * altura
litros = area / 2

print(f'A área total da sua parede é de {cores['verde']}{area:.2f}m{cores['limpa']}, são necessários {cores['amarelo']}{litros:.2f}L{cores['limpa']} de tinta para pintá-la!')