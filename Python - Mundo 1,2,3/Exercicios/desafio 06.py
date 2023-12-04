# num = int(input('Escreva um numero para saber o dobro, triplo e raiz quadrada: '))
# print(f'O dobro de {num} é: {num * 2} \nO triplo de {num} é: {num * 3} \ne a raiz quadrada de {num} é: {num **(1/2):.2f}')

n = int(input('Digite um numero para saber seu dobro, triplo e sua raiz quadrada: ').strip().upper())
c = ''
while True:
    print(f'O dobro de {n} é: {n * 2}\nO triplo de {n} é: {n * 3}\nA raiz quadrada de {n} é: {n ** (1 / 2):.2f}')
    c = str(input('Deseja saber os resultados de outro numero? Se sim digite [S] se não [N]: ').strip().upper())
    if c == 'S':
        n = int(input('Digite outro numero para saber seus resultados: ').strip().upper())
    elif c == 'N':
        break
print('Programa finalizado ...')
