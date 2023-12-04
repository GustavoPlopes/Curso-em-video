lista = []
contador = 0
valor_cinco = 0
while True:
    n = int(input(f'Digite um valor: '))
    lista.append(n)
    contador += 1
    if n == 5:
        valor_cinco += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N}? ')).strip().upper()
        print(f'{"":=^48}')
    if continuar == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {contador} números')
print(f'A lista de valores na ordem decrescente é ', end='')
for l in lista:
    print(f'{l} ', end='')
if 5 in lista:
    print(f'\nO valor 5 aparece {valor_cinco} vezes...')
else:
    print(f'\nO valor 5 não aparece na lista...')
