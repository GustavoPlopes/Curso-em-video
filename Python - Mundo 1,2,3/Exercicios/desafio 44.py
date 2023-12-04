print(f'{"LOJA GUSTAVO MARQUES":=^40}')
produto = float(input(f'Digite valor do seu produto: '))
pagamento = int(input('''===============================
Escolha a opção de pagamento
[1]- DINHEIRO/CHEQUE
[2]- 1x CARTÃO
[3]- 2x CARTÃO
[4]- 3X OU MAIS CARTÃO
===============================
Digite aqui a opção desejada>> '''))


if pagamento == 1:
    print(f'Você escolheu a opção DINHEIRO/CHEQUE seu produto que era R${produto:.2f} com 10% de desconto fica R${produto - (10 * produto / 100):.2f}')
elif pagamento == 2:
    print(f'Você escolheu a opção 1x CARTÃO seu produto que era R$ {produto:.2f} com o 5% de desconto fica {produto - (5 * produto / 100):.2f} ')
elif pagamento == 3:
    parcela = produto / 2
    print(f'Você escolheu a opção 2x CARTÃO de R${parcela:.2f} valor total do produto R${produto:.2f} ')
elif pagamento == 4:
    qts = int(input('Digite a quantidade de parcelas: '))
    total = produto + (20 * produto / 100)
    parcela = total / qts
    print(f'Você escolheu a opção  {qts}x de R${parcela:.2f} com 20% de jutos  valor do produto R${produto:.2f} com 20% de juros fica {produto + (20 * produto / 100):.2f}')
else:
    print('Opção invalida, tente novamente.')
