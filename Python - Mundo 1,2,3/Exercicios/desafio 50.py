print(f'\033[1:34:40m{"Digite seis numeros inteiros, sera considerado apenas números pares":=^100}\033[m')
s = 0
for x in range(1, 7):
    num = int(input(f'\033[1:35mDigite o numero {x}: '))
    if num % 2 == 0:
        s += num
print(f'O total é {s}')
