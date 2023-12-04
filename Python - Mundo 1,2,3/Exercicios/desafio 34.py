salario = float(input('Digite o seu salario para saber quanto ganhou de aumento: '))
if salario >= 1250:
    print(f'Seu novo salario com 10% de aumento é de R${float(10 * salario / 100) + salario:.2f}')
else:
    print(f'Seu novo salario com 15% de aumento é de R${float(15 * salario / 100) + salario:.2f}')
