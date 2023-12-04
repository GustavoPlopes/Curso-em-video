import time
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    opção = int(input('''Digite a opção desejada para saber o resultado
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR
    Qual a sua opção? >>> '''))
    if opção == 1:
        soma = valor1 + valor2
        print(f'Total: {valor1}+{valor2}={soma}')
    elif opção == 2:
        multiplicação = valor1 * valor2
        print(f'Total: {valor1}*{valor2}={multiplicação}')
    elif opção == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(f'O maior valor é {maior}')
    elif opção == 4:
        valor1 = int(input('Digite o novo primeiro valor: '))
        valor2 = int(input('Digite o novo segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        time.sleep(2)
    else:
        print('Opção invalida, tente novamente.')
print('Obrigado por usar o programa.')

