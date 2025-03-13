print('='*10,'DESAFIO 29','='*10)

velocidade = int(input('Digite a velocidade: '))

if velocidade >= 80.0:
    multa = (velocidade - 80) * 7
    print(f'Você excedeu o limite de 80km/h e foi multado em R$ {multa:.2f}.')
print('Tenha um bom dia e lembre-se: Dirija com segurança!')