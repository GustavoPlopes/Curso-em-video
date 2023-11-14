# # versão 1
# a = float(input('Escreva o cateto adjacente: '))
# b = float(input('Escreva o cateto oposto: '))
# c = (a**2 + b**2) ** (1/2)
# print(f'O total da hipotenusa: {c:.2f}')
#
# # versão 2
# import math
# a2 = float(input('Escreva o cateto adjacente: '))
# b2 = float(input('Escreva o cateto oposto: '))
# print(f'O total da hipotenusa é {math.hypot(a2, b2):.2f}')


from math import hypot
from time import sleep
calculo = []
hipotenusa = []
print(f'''{"":=^48}
{"CALCULE A HIPOTENUSA":^48}
{"":=^48}''')
while True:
    adj = float(input('Digite o cateto adjacente: '))
    calculo.append(adj)
    oposto = float(input('Digite o cateto oposto: '))
    calculo.append(oposto)
    hipotenusa.append(f'{hypot(adj, oposto):.2f}')
    print(f'''O total da hipotenusa é {hypot(adj, oposto):.2f}
{"":=^48}''')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja calcular outro valor da hipotenusa? [S/N]? ')).strip().upper()
    if continuar == 'N':
        break
print('Aguarda para ser exibido todos resultados...')
# sleep(3)
for h in range(0, len(calculo)):
    if h % 2 == 0:
        print(f'O calculo da hipotenusa do cateto adjacente {calculo[h]} ')
    else:
        for x in range(0, len(hipotenusa)):
            print(f'e do cateto oposto {calculo[h]} é {hipotenusa[x]}')

