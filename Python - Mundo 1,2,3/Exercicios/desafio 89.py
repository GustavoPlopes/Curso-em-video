# alunos = list()
#
# while True:
#     nome = str(input('Nome do aluno: '))
#     nota1 = float(input('Primeira nota: '))
#     nota2 = float(input('Segunda nota: '))
#     media = (nota1 + nota2) / 2
#     alunos.append([nome, [nota1, nota2], media])
#     continuar = ' '
#     while continuar not in 'SN':
#         continuar = str(input('Deseja adicionar nota de outro aluno? [S/N]? ')).strip().upper()
#     if continuar == 'N':
#         break
# print(f'{"":=^48}')
# print(f'{"NO.":<4}{"NOME":<10}{"MEDIA":>8}')
# for i, a in enumerate(alunos):
#     print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
# print(f'{"":=^48}')
# while True:
#     opc = int(input('Escolha o numero do aluno para exibir as notas, caso queira finalizar o programa digite 999:  '))
#     if opc == 999:
#         print('Programa finalizado...')
#         break
#     if opc <= len(alunos) - 1:
#         print(f'As notas do aluno {alunos[opc][0]} são {alunos[opc][1]}')

alunos = list()
while True:
    nome = str(input('Nome do aluno(a): '))
    nota1 = int(input('Primeira nota: '))
    nota2 = int(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja adicionar nota de outro aluno(a)? [S/N]? ')).strip().upper()
    if continuar == 'N':
        break
print(f'{"NO.":<4}{"NOME":<10}{"MEDIA":>10}')
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>10.1f}')
while True:
    opç = int(input('Deseja exibir as notas de qual aluno? digite o numero que está no indice,'
                    ' caso deseja sair digite 999:  '))
    if opç == 999:
        print('Programa finalizo, obrigado por usar!!!')
        break
    if opç <= len(alunos) -1:
        print(f'O aluno {alunos[opç][0]} obteve as notas {alunos[opç][1]}')

