# n1 = int(input('Digite o Primeiro numero: '))
# n2 = int(input('Digite o segundo numero: '))
# n3 = int(input('Digite o terceiro numero'))
# print(f'Numero maior {max(n1,n2,n3)}\nNumero menor {min(n1,n2,n3)}')

# versão 2
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor digitado é {maior}')
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor numero é {menor}')
