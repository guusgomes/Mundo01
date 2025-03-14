cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 04', '=' * 6, f'{cores['limpa']}')

n = input('Digite qualquer coisa: ')

print(f'{cores['verde']}O tipo primitivo do valor é',type(n))
print(f'{cores['vermelho']}É somente espaços?',n.isspace())
print(f'{cores['amarelo']}É letra?',n.isalpha())
print(f'{cores['azul']}É letra maiúscula?',n.isupper())
print(f'{cores['magenta']}É letra minúscula?',n.islower())
print(f'{cores['ciano']}É capitalizada?',n.istitle())
print(f'{cores['verde']}É alfanumérico?',n.isalnum())
print(f'{cores['vermelho']}É número?',n.isnumeric())