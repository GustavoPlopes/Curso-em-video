n = 0
c = 0
soma = 0
while True:
    n = int(input('Digite mais um numero ou 999 para finalizar: '))
    if n == 999:
        break
    soma += n
    c += 1
print(f'O programa identificou {c} numeros e a soma entre eles é de {soma}')