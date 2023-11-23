from modulos import moedas

n = float(input('Digite o valor: R$'))
print(f'A metade de {moedas.moeda(n):} é {moedas.moeda(moedas.metade(n))}')
print(f'O dobro de {moedas.moeda(n):} é {moedas.moeda(moedas.dobro(n))}')
print(f'Aumentando 10% de {moedas.moeda(n)} fica {moedas.moeda(moedas.aumento(n, 10))}')
print(f'Reduzindo 13% de {moedas.moeda(n)} fica {moedas.moeda(moedas.reduzindo(n, 13))}')

