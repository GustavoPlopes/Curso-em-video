# num = int(input(f'\033[1:4:30:44m{"Digite um número para saber se ele é primo":#^60}\033[m\nDigite o numero: '))
# print(f'Os números em \033[31mvermelho\033[m não são divisiveis por {num}, e os em \033[34mazul\033[m são')
# tot = 0
#
# for c in range(1, num + 1):
#     if num % c == 0:
#         print('\033[34m', end='')
#         tot += 1
#     else:
#         print('\033[31m', end='')
#     print(f'{c}', end=' ')
# print(f'\nO número {num} foi divisivel {tot} vezes')
# if tot == 2:
#     print('\033[34mÉ UM NÚMERO PRIMO\033[m')
# else:
#     print('\033[31mNÃO É UM NÚMERO PRIMO\033[m')

num = int(input('Digite um número: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'\nO número {num} é divisivel {tot} vezes\033[m')
if tot == 2:
    print('É um número primo')
else:
    print('Não é número primo')
