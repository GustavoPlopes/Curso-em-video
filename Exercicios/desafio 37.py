num = int(input('Digite um numero inteiro: '))
opção = int(input('''Escolha uma das bases para a conversão
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal
Digite sua opção aqui>> '''))

if opção == 1:
    print(f'{num} convertido para BINARIO é igual a {num:b}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é {num:o}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é {num:x}')
else:
    print('Opção invalida. Tente novamente !')
