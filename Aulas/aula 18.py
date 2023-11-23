# Exemplo 1

# teste = list()
# teste.append('Gustavo')
# teste.append(25)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# galera = [['joão', 18], ['ana', 33], ['Joaquim', 13], ['Maria', 45]]
# # print(galera[3][1])
#
# for p in galera:
#     # print(p)
#     # print(p[0])
#     # print(p[1])
#     print(f'{p[0]} tem {p[1]} anos de idade')

# Exemplo 2

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append((int(input('Idade: '))))
    galera.append(dado[:])
    dado.clear()
# print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        totmen += 1
        print(f'{p[0]} é menor de idade')

print(f'O total de maiores de idade é {totmai} e o total de menores é {totmen}')