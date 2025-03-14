'''TEXTO	FUNDO	NOME
30	40	Preto
31	41	Vermelho
32	42	Verde
33	43	Amarelo
34	44	Azul
35	45	Magenta
36	46	Ciano
37	47	Branco
90	100	Preto brilhante (cinza)
91	101	Vermelho brilhante
92	102	Verde brilhante
93	103	Amarelo brilhante
94	104	Azul brilhante
95	105	Magenta Brilhante
96	106	Ciano brilhante
97	107	Branco brilhante'''

#print('\033[4;39;45mOlá, Mundo!\033[m')
#print('\033[7;39;45mOlá, Mundo!\033[m')

#a = 3
#b = 5 
#print(f'Os valores são \033[32m{a}\033[m e \033[34m{b}\033[m!!')

nome = str(input('Digite o seu nome: '))
cores = {'limpa':'\033[m',
        'verde':'\033[32m',
        'azul':'\033[34m'}

print(f'{cores["azul"]}Seu nome é {cores["verde"]}{nome}{cores["azul"]}!!')