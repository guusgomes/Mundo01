from random import shuffle
print('='*6,'DESAFIO 20','='*6)
a1 = input('Nome do aluno: ')
a2 = input('Nome do aluno: ')
a3 = input('Nome do aluno: ')
a4 = input('Nome do aluno: ')
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print(f'A ordem de apresentação é: {alunos}.')