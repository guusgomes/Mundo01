print('='*10,'DESAFIO 35','='*10)

r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite outro comprimento: '))
r3 = float(input('Digite o último comprimento: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas digitadas formam um triângulo!')
else:
    print('As retas digitadas NÃO formam um triângulo!')