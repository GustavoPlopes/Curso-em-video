from modulos import moedas

n = float(input('Digite o preço: R$'))
print(f'A metade de R${n} é R${moedas.metade(n)}')
print(f'O dobro de R${n} é R${moedas.dobro(n)}')
print(f'Aumentando 10% de R${n} fica R${moedas.aumento(n)}')
print(f'Reduzindo 13% de R${n} fica R${moedas.reduzindo(n)}')
