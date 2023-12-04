# versão 1
import math
ang = float(input('Qual o angulo: '))
rad = math.radians(ang)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print(f'O angulo {ang} tem o seno {seno:.2f}, cosseno {cosseno:.2f} e a tangente {tangente:.2f}')

# Versão 2
from math import radians, sin, cos, tan
ang = float(input('Escreva o angulo:'))
rad = radians(ang)
print(f'O angulo {ang} tem o seno de {sin(rad):.2f}, cosseno de {cos(rad):.2f} e a tangente de {tan(rad):.2f} ')