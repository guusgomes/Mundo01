cores = {'limpa':'\033[m',
         'titulo':'\033[1;31;47m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'ciano':'\033[1;36m'}

print(f'{cores['titulo']}', '=' * 6, 'DESAFIO 24', '=' * 6, f'{cores['limpa']}')

cidade = str(input('Digite o nome da sua cidade: ')).strip().split()
primeira = cidade[0].upper()
santo = str(primeira.count('SANTO'))

print(f'Sua cidade{cores['vermelho']}{santo.replace('1',' ').replace('0',' não ')}começa{cores['limpa']} com "Santo".')