# from random import randint
# v = 0
# while True:
#     print('Te desáfio para jogar impar ou par!!!')
#     jgd = int(input('Faça sua jogada: '))
#     pc = randint(0,10)
#     total = jgd + pc
#     pi = ' '
#     while pi not in 'PI':
#         pi = str(input('Digite [P] para par ou [I] para impar: ')).strip().upper()
#         print(f'computador jogou {pc} e jogador jogou {jgd}, total de {total}')
#         print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
#     if pi == 'P':
#         if total % 2 == 0:
#             print('venceu')
#             v += 1
#         else:
#             print('perdeu')
#             break
#     if pi == 'I':
#         if total % 2 == 1:
#             print('Venceu')
#             v += 1
#         else:
#             print('perdeu')
#             break
#     print('Vamos jogar novamente')
# print(f'GAME OVER! Você venceu {v}', "vezes." if v > 1 else "vez.")

from random import randint

while True:
    print('=========Vamos jogar Impar Ou Par============')
    jgd = int(input('Faça sua jogada: '))
    pc = randint(0, 10)
    total = jgd + pc
    option = ' '
    v = 0
    while option not in 'PI':
        option = str(input('[p] para Par ou [I] para impar ')).strip().upper()
        print(f'O jogador jogou {jgd} e o computador jogou {pc}, total de {total},', 'DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if option == 'P':
        if total % 2 == 0:
            print('PARABÉNS!! Você venceu.')
            v += 1
        else:
            print('QUE PENA!! Você perdeu.')
            break
    if option == 'I':
        if total % 2 == 1:
            print('PARABÉNS!! Você venceu.')
            v += 1
        else:
            print('QUE PENA!! Você perdeu.')
            break

print(f'GAME OVER!! Você venceu {v}','vezes.' if v > 1 else 'vez')
