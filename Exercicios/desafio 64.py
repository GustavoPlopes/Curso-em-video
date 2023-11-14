n = int(input('Digite um numero: '))
c = 0
soma = 0
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um novo numero ou 999 para finalizar o programa e mostrar o total: '))
print(f'Você digitou {c} numeros e a soma de todos eles é {soma}')