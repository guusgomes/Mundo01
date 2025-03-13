print('='*10,'DESAFIO 31','='*10)

distancia = float(input('Qual a distância da viagem? '))

if distancia <= 200.00:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

print(f'O valor da passagem para {distancia:.2f}km é: R$ {valor:.2f}.')