print('='*10,'DESAFIO 26','='*10)

frase = str(input('Digite uma frase: ')).strip().upper()

print(f'Na frase: "{frase.capitalize()}":')
print(f'A letra "A" aparece {frase.count('A')} vez(es).')
print(f'A letra "A" aparece primeiro na posição {frase.find('A')}.')
print(f'A letra "A" aparece por último na posição {frase.rfind('A')}.')