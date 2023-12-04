# matriz = list()
# dados = list()
# for m in range(0, 3):
#     for x in range(0, 3):
#         dados.append(int(input('Digite um valor: ')))
#     matriz.append(dados[:])
#     dados.clear()
#
# for c in range(0, len(matriz)):
#     print(f'[{matriz[0][c]}]', end=' ')
# print()
# for c in range(0, len(matriz)):
#     print(f'[{matriz[1][c]}]', end=' ')
# print()
# for c in range(0, len(matriz)):
#     print(f'[{matriz[2][c]}]', end=' ')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for n in range(0, 3):
        matriz[l][n] = int(input(f'Digite um numero para posição |{l}, {n}|: '))
print(f'{"":=^48}')
for l in range(0, 3):
    for n in range(0, 3):
        print(f'[{matriz[l][n]:^5}]', end='')
    print()
print(f'{"":=^48}')
