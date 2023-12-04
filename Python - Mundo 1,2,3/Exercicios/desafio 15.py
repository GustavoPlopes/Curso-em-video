# dias = int(input('Quantos dias alugados: '))
# km = float(input('Quantos Km rodados: '))
# pagar = dias * 60 + km * 0.15
# print(f'O total a pagar é de R${pagar:.2f} e pagando a vista com desconto de 10% {pagar - pagar * 10 / 100:.2f}')


veiculos = []
print(f'''{"":=^48}
{"ALUGA-SE VEÍCULOS":^48}
{"":=^48}''')
dias = 0
km = 0
while True:
    automovel = str(input('Qual veículo deseja alugar? '))
    veiculos.append(automovel)
    dias = int(input('Quantos dias pretende alugar? '))
    km = int(input('Quantos Km pretende rodar? '))
    pagar = dias * 60 + km * 0.15
    veiculos.append(pagar)
    print(f'''O total a pagar é R${pagar:.2f} pagando a vista com desconto 10% fica {pagar - 10 * pagar / 100:.2f}
{"":=^48}''')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja adicionar outro veiculo? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'{"":=^48}')
for v in range(0, len(veiculos)):
    if v % 2 == 0:
        print(f'O veiculo {veiculos[v]} fica no valor de ', end='')
    else:
        print(f'R${veiculos[v]:.2f} com desconto de 10% no pagamento a vista fica '
              f'{veiculos[v] - 10 * veiculos[v] / 100}')
print(f'{"":=^48}')
