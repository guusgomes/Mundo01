from math import radians, sin, cos, tan
print('='*6,'DESAFIO 18','='*6)
n = int(input('Digite o valor de um ângulo: '))
seno = sin(radians(n))
cosseno = cos(radians(n))
tangente = tan(radians(n))
print(f'Você digitou {n}º, o seno é {seno:.2f}, o cosseno é {cosseno:.2f} e a tangente é {tangente:.2f}.')