lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja digitar outro numero? [S/N]? ')).strip().upper()
    if continuar == 'N':
        break
print(f'A lista contem os valores pares, ', end='')
for l in range(0, len(lista)):
    if lista[l] % 2 == 0:
        print(f'{lista[l]} ',end='')
print(f'\nA lista contem os valores impares, ', end='')
for l in range(0, len(lista)):
    if lista[l] % 2 == 1:
        print(f'{lista[l]} ', end='')