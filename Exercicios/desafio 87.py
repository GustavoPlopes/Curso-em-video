print(f'''{"":=^58}
DIGITE OS NÚMEROS QUE DESEJA PARA SABER A SOMA DOS PARES, 
   DA TERCEIRA COLUNA E O MAIOR VALOR DA SEGUNDA LINHA.
{"":=^58}''')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somatvp = somatc = maior = 0
for l in range(0, 3):
    for n in range(0, 3):
        matriz[l][n] = int(input(f'Digite o numero para |{l}, {n}|: '))
        if matriz[l][n] % 2 == 0:
            somatvp += matriz[l][n]
print(f'{"":=^48}')
for l in range(0, 3):
    for n in range(0, 3):
        print(f'[{matriz[l][n]:^5}]', end='')
    print()
print(f'{"":=^48}')
print(f'A soma de todos valores pares digitados é {somatvp}')
for c in range(0, 3):
    somatc += matriz[c][2]
print(f'A soma dos valores da terceira coluna é {somatc}')
for l in range(0, 3):
    if l == 0:
        maior = matriz[1][l]
    elif matriz[1][l] > maior:
        maior = matriz[1][l]
print(f'O maior valor da segunda linha é {maior}')
