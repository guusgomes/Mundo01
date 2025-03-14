##from math import pow, sqrt
##co = float(input('Comprimento do cateto oposto: '))
##ca = float(input('Comprimento do cateto adjacente: '))
##hi = sqrt(pow(co, 2) + pow(ca, 2))
##print(f'O comprimento da hipotenusa é {hi:.2f}.')

from math import hypot
cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 11', '=' * 6, f'{cores['limpa']}')

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)

print(f'O comprimento da {cores['vermelho']}hipotenusa{cores['limpa']} é {cores['amarelo']}{hi:.2f}{cores['limpa']}.')

##co = float(input('Comprimento do cateto oposto: '))
##ca = float(input('Comprimento do cateto adjacente: '))
##hi = (co ** 2 + ca ** 2) ** (1/2)
##print(f'O comprimento da hipotenusa é {hi:.2f}.')