# from time import sleep
# n = int(input('Digite um numero para saber o fatorial: '))
# c = n
# f = 1
# print(f'Calculando...')
# sleep(2)
# print(f'{n}! =', end='')
# while c > 0 :
#   print(f'{c}', 'x ' if c > 1 else '= ', end='')
#   f *= c
#   c -= 1
# print(f'{f}')


n = int(input('Digite um numero para saber seu fatorial: '))
c = n
f = 1
for c in range(n, 0, -1):
  print(f'{c}', 'x ' if c > 1 else '= ', end='')
  f *= c
  c -= 1
print(f'{f}')


