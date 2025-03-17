cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 23', '=' * 6, f'{cores['limpa']}')

n = int(input('Digite um número inteiro de 0 a 9999: '))
unidade = n % 10
dezena = (n // 10) % 10
centena = (n // 100) % 10
milhar = (n // 1000) % 10

print(f'Unidade: {cores['amarelo']}{unidade}{cores['limpa']}')
print(f'Dezena: {cores['vermelho']}{dezena}{cores['limpa']}')
print(f'Centena: {cores['verde']}{centena}{cores['limpa']}')
print(f'Milhar: {cores['azul']}{milhar}{cores['limpa']}')