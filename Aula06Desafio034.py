cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 34', '=' * 6, f'{cores['limpa']}')

salario = float(input('Digite o salário atual: R$ '))

if salario >= 1250.00:
    novosalario = salario + (salario * 0.10)
else:
    novosalario = salario + (salario * 0.15)

print(f'Seu salário após o aumento é: {cores['azul']}R$ {novosalario:.2f}{cores['limpa']}!')