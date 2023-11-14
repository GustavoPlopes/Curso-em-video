# Versão 1
# import random
# a1 = input('Aluno 1: ')
# a2 = input('Aluno 2: ')
# a3 = input('Aluno 3: ')
# a4 = input('Aluno 4: ')
# alunos = [a1, a2, a3, a4]
# sorteio = random.choice(alunos)
# print(f'O aluno sorteado é {sorteio}')

# Versão 2
from random import choice
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
alunos = [a1, a2, a3, a4]
print(f'O aluno sorteado é {choice(alunos)}')
