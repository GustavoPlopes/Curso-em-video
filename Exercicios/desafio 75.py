
num = (int(input('Digite o 1º número: ')),
       int(input('Digite o 2º número: ')),
       int(input('Digite o 3º número: ')),
       int(input('Digite o 4º número: ')))

print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
       print(f'O número 3 foi digitado primeiro na {num.index(3)}º posição')
else:
       print('O numero 3 não apareceu em nenhuma posição')
print('Os Números pares foram ', end='')
for n in num:
       if n % 2 == 0:
              print(n, end=' ')
