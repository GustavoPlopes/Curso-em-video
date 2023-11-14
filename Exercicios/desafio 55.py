# maior = 0
# menor = 0
# for x in range(1, 6):
#     peso = float(input(f'Escreva o peso da {x}º pessoa: '))
#     if x == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print(f'O maior peso é {maior}Kg\nE o menor peso é {menor}Kg')
maior = 0
menor = 0

for x in range(1, 6):
    peso = float(input(f'Digite o peso da {x}º pessoa: '))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O mair peso é {maior}Kg\nE o menor peso é {menor}Kg')