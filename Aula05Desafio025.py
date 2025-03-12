print('='*10,'DESAFIO 25','='*10)

nome = str(input('Digite seu nome completo: ')).strip().upper()
silva = str(nome.count('SILVA'))

print(f'Seu nome{silva.replace('1',' ').replace('0', ' não ')}possui "Silva".')