from random import shuffle

cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 11', '=' * 6, f'{cores['limpa']}')

a1 = input('Nome do aluno: ')
a2 = input('Nome do aluno: ')
a3 = input('Nome do aluno: ')
a4 = input('Nome do aluno: ')
alunos = [a1, a2, a3, a4]
shuffle(alunos)

print(f'A ordem de apresentação é: {cores['amarelo']}{alunos}{cores['limpa']}.')