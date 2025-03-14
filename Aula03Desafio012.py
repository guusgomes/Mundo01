cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 12', '=' * 6, f'{cores['limpa']}')

preco = float(input('Digite o valor do produto: R$ '))
novopreco = preco - (preco * 0.05) 

print(f'O valor do produto com desconto é: {cores['vermelho']}R$ {novopreco:.2f}{cores['limpa']}.')