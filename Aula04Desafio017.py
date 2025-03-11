##from math import pow, sqrt
print('='*6,'DESAFIO 17','='*6)
##co = float(input('Comprimento do cateto oposto: '))
##ca = float(input('Comprimento do cateto adjacente: '))
##hi = sqrt(pow(co, 2) + pow(ca, 2))
##print(f'O comprimento da hipotenusa é {hi:.2f}.')

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'O comprimento da hipotenusa é {hi:.2f}.')

##co = float(input('Comprimento do cateto oposto: '))
##ca = float(input('Comprimento do cateto adjacente: '))
##hi = (co ** 2 + ca ** 2) ** (1/2)
##print(f'O comprimento da hipotenusa é {hi:.2f}.')