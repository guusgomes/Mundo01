from random import choice
print('='*6,'DESAFIO 19','='*6)
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
alunos = [a1, a2, a3, a4]
escolhido = choice(alunos)
print(f'O(A) aluno(a) selecionado(a) foi {escolhido}!')