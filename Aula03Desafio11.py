print('='*6,'DESAFIO 11','='*6)
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
litros = area / 2
print(f'A área total da sua parede é de {area:.2f}m², são necessários {litros:.2f}L de tinta para pintá-la!')