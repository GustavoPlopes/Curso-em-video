#
# total_compra = produto_mais_barato = mais_de_mil = cont = 0
# barato = ''
# print(f'''{"CASAS BAHIA":=^40}''')
# while True:
#     nome_produto = str(input('Insira o nome do produto: ')).strip()
#     preço_produto = float(input('Insira o valor do seu produto: R$').strip())
#     cont += 1
#     total_compra += preço_produto
#     print(f'{"":=^40}')
#     if preço_produto > 1000:
#         mais_de_mil += 1
#     if cont == 1:
#         produto_mais_barato = preço_produto
#         barato = nome_produto
#     else:
#         if preço_produto < produto_mais_barato:
#             produto_mais_barato = preço_produto
#             barato = nome_produto
#     continuar = ' '
#     while continuar not in 'SN':
#         continuar = str(input('Deseja continuar inserindo outros produtos?\nSe sim digite [S] se não [N]: ')).strip().upper()[0]
#     if continuar == 'N':
#         break
#
# print(f'{"":=^40}\nO valor total da compra é de R${total_compra:.2f}')
# print(f'{mais_de_mil} dos seus produtos custam mais de R$1000,00')
# print(f'O produto mais barato é {barato} que custa R${produto_mais_barato:.2f}\n{"":=^40}')]

total_gasto = mais_de_mil = mais_barato = cont = 0
barato = ''
print(f'{"LOJA MARQUES":=^40}')
while True:
    nome_produto = str(input('Insira o nome do produto: '))
    preço_produto = float(input('Valor: R$'))
    print(f'{"":=^63}')
    total_gasto += preço_produto
    cont += 1
    if preço_produto > 1000:
        mais_de_mil += 1
    if cont == 1:
        mais_barato = preço_produto
        barato = nome_produto
    elif preço_produto < mais_barato:
        mais_barato = preço_produto
        barato = nome_produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Se deseja continuar adicionando produtos digite [S] se não [N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total gasto na compra é de R${total_gasto:.2f}')
print(f'Total de {mais_de_mil} produtos custam mais de R$1000,00.')
print(f'O nome do produto mais barato é {barato} e o valor é R${mais_barato:.2f}')
