velocidade = int(input('Digite a velocidade: ').strip())
if velocidade > 80:
    print(f'Você foi multado por passar no pardal à {velocidade}Km, excedeu {velocidade - 80}'
          f'Km do permitido\nA multa custa R$7,00 por Km excedido, valor a pagar de: R${(float(velocidade - 80) * 7):.2f}')
else:
    print('Você não excedeu a velocidade permitida!')