# nota1 = float(input('Escreva a nota do 1 bimestre para calcular a media:'))
# nota2 = float(input('Nota do segundo bimestre: '))
# print(f' Sua media é: {(nota1 + nota2) /2:.1f}')


n = 0
t = 0

while True:
    print(f'''\033[1:34m{"CALCULADORA DE MEDIA DOS 4 BIMESTRES":-^50}\033[m
\033[1:31mobs: caso deseje finalizar o programa digite [S] de sair.\033[m''')
    name = str(input('\033[1:34mQual seu nome\033[m? ')).strip().upper()
    if name == 'S':
        break
    for x in range(1, 5):
        n = float(input(f'Digite a {x} nota: '))
        t += n
    media = t / 4
    if media >= 6.00:
        print(f'\033[1:32mPARABÉNS {name}, APROVADO!!!! Sua media foi de {media:.2f}\033[m')
    else:
        print(f'\033[1:31mQUE PENA, {name}, REPROVADO!!! Sua media foi de {media:.2f}\033[m')
