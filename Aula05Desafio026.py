cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 26', '=' * 6, f'{cores['limpa']}')

frase = str(input('Digite uma frase: ')).strip().upper()

print(f'Na frase: "{frase.capitalize()}":')
print(f'A letra {cores['amarelo']}"A"{cores['limpa']} aparece {cores['amarelo']}{frase.count('A')}{cores['limpa']} vez(es).')
print(f'A letra {cores['amarelo']}"A"{cores['limpa']}  aparece primeiro na posição {cores['amarelo']}{frase.find('A') + 1}{cores['limpa']}.')
print(f'A letra {cores['amarelo']}"A"{cores['limpa']}  aparece por último na posição {cores['amarelo']}{frase.rfind('A') + 1}{cores['limpa']}.')