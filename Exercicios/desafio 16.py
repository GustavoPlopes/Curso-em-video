# Versão 1
import math
real = float(input('Escreva um numero real: '))
print(f'O numero {real} tem a parte inteira {math.trunc(real)}')

# versão 2
from math import trunc
real = float(input('Escreva um numero real: '))
print(f'O numero {real} tem a parte inteira {trunc(real)}')

# Versão 3
real = float(input('Escreva um numero real: '))
print(f'O numero {real} tem a parte inteira {int(real)}')
