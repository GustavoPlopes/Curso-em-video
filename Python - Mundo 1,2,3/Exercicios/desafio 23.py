# n = input('Escreva um numero para mostrar cada digito separado: ')
# print(f'Em unidade: {n[3]}\nEm dezena: {n[2]}\nEm centena {n[1]}\nEm milhar {n[0]} ')

num = int(input('Escreva um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o numero {num}\nUnidade {u}\nDezena {d}\nCentena {c}\nMilhar {m}')