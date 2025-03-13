#print('='*10,'DESAFIO 22','='*10)

#nome = str(input('Digite seu nome completo: ')).strip()
#palavras = nome.split()

#print(f'Minúsculo: {nome.lower()}')
#print(f'Maiúsculo: {nome.upper()}')
#print(f'O nome completo tem {len(nome) - nome.count(' ')} letras!')
#print(f'O primeiro nome tem {len(palavras[0])} letras!')

print('='*10,'DESAFIO 22','='*10)

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Minúsculo: {nome.lower()}')
print(f'Maiúsculo: {nome.upper()}')
print(f'O nome completo tem {len(nome) - nome.count(' ')} letras!')
print(f'O primeiro nome tem {nome.find(' ')} letras!')