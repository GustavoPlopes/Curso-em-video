soma = 0
cont = 0
for multiplos in range(1, 501, 2):
    if multiplos % 3 == 0:
        soma += multiplos
        cont += 1
print(f'A soma de todos esses {cont} valores é  {soma}')
