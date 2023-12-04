# preco = float(input('Escrava o valor do produto para calcular o novo preço com 5% de desconto: R$'))
# print(f'O valor de R${preco:.2f} com 5% de desconto é de R${preco - (preco * 5.0 / 100):.2f} ')

from time import sleep
while True:
    option = int(input('''Escolha uma opção de pagamento
[1] Dinheiro a vista
[2] 1x no credito
[3] 2x no credito
[4] 3x no credito
[5] 4x ou mais

[0] Finalizar
Digite sua opção aqui >>> '''))
    if option == 0:
        break
    valor = float(input('Digite o valor do produto: '))
    if option == 1:
        print(f'{"="*80}')
        print(f'Opção dinheiro a vista com 20% de desconto, valor total com desconto: R${valor - (valor * 20 / 100):.2f}')
        print(f'{"=" * 80}\n')
    elif option == 2:
        print(f'''{"="*80}
Opção 1x no credito com 15% de desconto, o valor total com desconto: R${valor - (valor * 15 / 100):.2f}
{"="*80}\n''')
    elif option == 3:
        print(f'''{"="*80}
Opção 2x no credito com 10% de desconto, valor total com desconto: R${valor -(valor * 10 / 100):.2f}
{"="*80}\n''')
    elif option == 4:
        print(f'''{"="*80}
Opção 3x no credito com 5% de desconto, valor total com desconto: R${valor - (valor * 5 / 100):.2f}
{"="*80}\n''')
    elif option == 5:
        print(f'''{"="*80}
Opção 4x ou mais sem juros, valor total sem juros: R${valor:.2f}
{"="*80}''')

print('Aguarde, finalizando programa ...')
sleep(3)
print('Programa finalizado')


