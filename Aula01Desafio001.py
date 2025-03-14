cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m'}

print(f'{cores['titulo']}', '=' * 6,'DESAFIO 01', '=' * 6, f'{cores['limpa']}')

nome = input('Qual é o seu nome? ')

print(f'Olá {cores['verde']}{nome}{cores['limpa']}! Prazer em te conhecer!')