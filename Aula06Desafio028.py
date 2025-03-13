from random import randint
print('='*10,'DESAFIO 28','='*10)

numeropc = randint(0, 5)
numeropessoa = int(input('Pensei em um número de 0 a 5, que número é esse? '))

if numeropessoa == numeropc:
    print('Parabéns, você acertou!')
else:
    print(f'Você errou, eu pensei no número {numeropc}!')