print('='*10,'DESAFIO 24','='*10)

cidade = str(input('Digite o nome da sua cidade: ')).strip().split()
primeira = cidade[0].upper()
santo = str(primeira.count('SANTO'))

print(f'Sua cidade{santo.replace('1',' ').replace('0',' não ')}começa com "Santo".')