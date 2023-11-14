# from random import randint
# aleatório = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# print('Os numeros sorteados são:', end='')
# for n in aleatório:
#     print(f'{n}', end=' ')
# print(f'\nO maior valor sorteado foi {max(aleatório)}')
# print(f'O menor valor sorteado foi {min(aleatório)}')

from random import randint
aleatório = (randint(1, 10), randint(1, 10), randint(1, 10),
             randint(1, 10), randint(1, 10))
print('Os numeros sorteados são: ', end='')
for n in aleatório:
    print(f'{n}', end=' ')
print(f'''\nO maior numero sorteado é {max(aleatório)}
O menor numero é {min(aleatório)}''')
