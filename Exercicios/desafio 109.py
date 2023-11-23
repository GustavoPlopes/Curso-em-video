from modulos import moedas

n = float(input('Digite o valor: R$'))
print(f'A metade de {moedas.moeda(n):} é {moedas.metade(n, True)}')
print(f'O dobro de {moedas.moeda(n):} é {moedas.dobro(n, True)}')
print(f'Aumentando 10% de {moedas.moeda(n)} fica {moedas.aumento(n, 10, True)}')
print(f'Reduzindo 13% de {moedas.moeda(n)} fica {moedas.reduzindo(n, 13, True)}')
