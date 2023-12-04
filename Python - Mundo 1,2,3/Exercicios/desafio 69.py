# maior = 0
# homens = 0
# mulheres = 0
# plural_homem = ' '
# plural_mulher = ' '
# while True:
#     age = int(input('Qual a sua idade? '))
#     sex = ' '
#     while sex not in 'MF':
#         sex = str(input('Qual seu sexo? [M/F]? ')).strip().upper()
#     if age > 18:
#         maior += 1
#     if sex == 'M':
#         homens += 1
#     if sex == 'F' and age < 20:
#         mulheres += 1
#     option = ' '
#     while option not in 'SN':
#         option = str(input('Quer adicionar idade e sexo de outra pessoa? [S/N]? ')).strip().upper()
#     if option == 'N':
#         break
#
# print(f'Foram registradas {maior} pessoas com mais de 18 anos.')
# print(f'Foram cadastrados {homens} homens.')
# print(f'Foram registradas {mulheres} {plural_mulher}com menos de 20 anos')


bigger = man = woman = 0

while True:
    print('\033[1:31:40m-------PESSOA--------\033[m')
    age = int(input(f'Qual a sua idade? '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input(f'Qual seu sexo? [M/F]? ')).strip().upper()
    if age > 18:
        bigger += 1
    if sex == 'M':
        man += 1
    if sex == 'F' and age < 20:
        woman += 1
    option = ' '
    while option not in 'SN':
        option = str(input('Deseja adicionar dados de mais uma pessoa? [S/N]?')).strip().upper()
    if option == 'N':
        break

print(f'''{"="*70}
Foram cadastradas {bigger} pessoas com mais de 18 anos.
Foram cadastrados {man} homens.
Foram cadastradas {woman} mulheres com menos de 20 anos.
{"="*70}''')
