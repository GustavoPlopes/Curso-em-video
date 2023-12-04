# import datetime
# maior = 0
# menor = 0
# for x in range(1,8):
#     ano = int(input(f'Digite o ano de nascimento da pessoa {x}: '))
#     idade = datetime.date.today().year - ano
#     if idade >= 21:
#         maior += 1
#     elif idade < 21:
#         menor += 1
# print(f'Ao todo foram {maior} pessoas maiores de idade\nE {menor} pessoas menores de de idade')

import datetime
maior = 0
menor = 0
for x in range(1, 8):
    ano = int(input(f'\033[1:4:35mDigite o ano de nascimento da {x}º pessoa\033[m: '))
    idade = datetime.date.today().year - ano
    if idade >= 21:
        maior += 1
        print(f'\033[31mA {x}º pessoa é maior e tem {idade} anos de idade\033[m')
    else:
        menor += 1
        print(f'\033[32mA {x}º pessoa é menor e tem {idade} anos de idade\033[m')
print(f'\n\033[30:44mAo total são {maior} pessoas maiores de idade\nE {menor} pessoas menores de idade\033[m')
