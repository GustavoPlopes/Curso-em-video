# salario = float(input('Digite o seu salario para calcular os 15% de aumento: R$'))
# aumento = salario * 15 / 100
# print(f'Antigo salario R${salario:.2f}\nseus 15% de aumento R${aumento:.2f}\nNovo salario R${salario + aumento:.2f}')

lista = []

print(f'''{"":=^48}
\033[1:32m{"CALCULADORA DE AUMENTO DE 15%":^48}\033[m
{"":=^48}''')
while True:
    nome = str(input('Qual seu nome? ')).strip().title()
    lista.append(nome)
    salario = float(input('Digite o seu salario: R$'))
    aumento = salario * 15 / 100
    lista.append(aumento+salario)
    print(f'{nome} seu antigo salario é R${salario:.2f} e o novo passa a ser {salario + aumento:.2f}')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        print(f'{"":=^48}')
    if continuar == 'N':
        break
for l in range(0, len(lista)):
    if l % 2 == 0:
        print(f'{lista[l]}, aumento de ', end='')
    else:
        print(f'R${lista[l]:.2f}')
print(f'{"":=^48}')