#print('='*10,'DESAFIO 22','='*10)

#nome = str(input('Digite seu nome completo: ')).strip()
#palavras = nome.split()

#print(f'Minúsculo: {nome.lower()}')
#print(f'Maiúsculo: {nome.upper()}')
#print(f'O nome completo tem {len(nome) - nome.count(' ')} letras!')
#print(f'O primeiro nome tem {len(palavras[0])} letras!')

cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 11', '=' * 6, f'{cores['limpa']}')

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Minúsculo: {cores['amarelo']}{nome.lower()}{cores['limpa']}')
print(f'Maiúsculo: {cores['verde']}{nome.upper()}{cores['limpa']}')
print(f'O nome completo tem {cores['vermelho']}{len(nome) - nome.count(' ')}{cores['limpa']} letras!')
print(f'O primeiro nome tem {cores['azul']}{nome.find(' ')}{cores['limpa']} letras!')