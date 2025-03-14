cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 25', '=' * 6, f'{cores['limpa']}')

nome = str(input('Digite seu nome completo: ')).strip().upper()
silva = str(nome.count('SILVA'))

print(f'Seu nome{cores['amarelo']}{silva.replace('1',' ').replace('0', ' não ')}possui{cores['limpa']} "Silva".')