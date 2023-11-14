# lista = []
# print(f'''{"":=^48}
# {"DIGITE 7 VALORES PARA SABER OS PARES E OS IMPARES":^48}
# {"":=^48}''')
# for c in range(0, 7):
#     lista.append(int(input(f'Digite o {c+1}º valor: ')))
#     lista.sort()
# print(f'Os números pares são ', end='')
# for p in range(0, len(lista)):
#     if lista[p] % 2 == 0:
#         print(f'{lista[p]} ', end='')
# print(f'\nOs números impares são ', end='')
# for i in range(0, len(lista)):
#     if lista[i] % 2 == 1:
#         print(f'{lista[i]} ', end='')


lista = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'''Os números pares são {lista[0]}
os números impares são {lista[1]}''')
