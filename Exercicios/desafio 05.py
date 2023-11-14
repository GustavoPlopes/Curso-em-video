# num = int(input('Escreva um numero para saber o sucessor e o antecessor:'))
# print(f'O sucessor de {num} é>> {num + 1} \ne o antecessor de {num} é>> {num - 1}')

n = int(input('Digite um numero para saber seus próximos sucessores e antecessores: '))
c = int(input('Quantos você quer que mostre?'))
sucessor = n
antecessor = n
for x in range(c ):
    if sucessor:
        sucessor += 1
    print(f'Sucessores: {sucessor}')
    if antecessor:
        antecessor -= 1
    print(f'Antecessores: {antecessor}')


