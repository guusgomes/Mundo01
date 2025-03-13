print('='*10,'DESAFIO 34','='*10)

salario = float(input('Digite o salário atual: R$ '))

if salario >= 1250.00:
    novosalario = salario + (salario * 0.10)
else:
    novosalario = salario + (salario * 0.15)

print(f'Seu salário após o aumento é: R$ {novosalario:.2f}!')