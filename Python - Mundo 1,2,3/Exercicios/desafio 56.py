# somaidade = 0
# mediaidade = 0
# maisvelho = 0
# nomemaisvelho = ''
# mulhermenosde20 = 0
# for p in range(1, 5):
#     print(f'\033[1:7:40m{f"{p}º PESSOA":=^40}\033[m')
#     nome = str(input(f'Nome da {p}º pessoa: '))
#     idade = int(input(f'Idade da {p}º pessoa: '))
#     sexo = str(input(f'Digite F para feminino e M para Masculino: '))
#     somaidade += idade
#
#     if p == 1 and sexo in 'Mm':
#         maisvelho = idade
#         nomemaisvelho = nome
#     if sexo in 'Mm' and idade > maisvelho:
#         maisvelho = idade
#         nomemaisvelho = nome
#     if sexo in 'Ff' and idade < 20:
#         mulhermenosde20 += 1
#
# mediaidade = somaidade // 4
# print(f'A média da idade do grupo é {mediaidade} anos de idade')
# print(f'O nome do Homem mais velho é {nomemaisvelho} e tem {maisvelho} anos de idade')
# print(f'A quantidade de mulheres que tem menos de 20 no grupo é de {mulhermenosde20}')

somaidade = 0
mediaidade = 0
maisvelho = 0
nomemaisvelho = ''
mulhermenosde20 = 0
for p in range(1, 5):
    print(f'{f"{p}º PESSOA":+^40}')
    nome = str(input(f'Nome da {p}º pessoa: ').strip())
    idade = int(input(f'Idade da {p}º pessoa: '))
    sexo = str(input(f'Digite F para Feminino e M para Masculino: '))
    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhermenosde20 += 1

mediaidade = somaidade // 4
print(f'A media da idade do grupo é de {mediaidade}')
print(f'O homem mais velho é o {nomemaisvelho} que tem {maisvelho} anos de idade')
print(f'Ao todo são {mulhermenosde20} mulher(es) com menos de 20')
