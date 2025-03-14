cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 02', '=' * 6, f'{cores['limpa']}')
print('Qual sua data de nascimento? ')

dia = input('Dia = ')
mes = input('Mes = ')
ano = input('Ano = ')

print(f'Você nasceu no dia {cores['vermelho']}{dia}{cores['limpa']} de {cores['vermelho']}{mes}{cores['limpa']} de {cores['vermelho']}{ano}{cores['limpa']}. {cores['verde']}Correto{cores['limpa']}?')