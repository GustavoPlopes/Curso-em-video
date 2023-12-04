# versão 1
# import random
# a1 = input('Aluno 1: ')
# a2 = input('Aluno 2: ')
# a3 = input('Aluno 3: ')
# a4 = input('Aluno 4: ')
# alunos = [a1, a2, a3, a4]
# random.shuffle(alunos)
# print(f'A ordem de apresentação do trabalho é {alunos}')

# versão 2
from random import shuffle
al1 = input('Aluno 1: ')
al2 = input('Aluno 2: ')
al3 = input('Aluno 3: ')
al4 = input('Aluno 4: ')
alunos = [al1, al2, al3, al4]
shuffle(alunos)
print(f'A ordem de apresentação é {alunos}')


