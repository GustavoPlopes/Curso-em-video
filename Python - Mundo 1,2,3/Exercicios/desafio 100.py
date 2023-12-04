# from random import randint
# números = list()


# def sorteia():
#     n = 0
#     soma = 0
#     for v in range(0, 5):
#         n = randint(0, 10)
#         if n % 2 == 0:
#             soma += n
#         números.append(n)
#     print(f'''Sorteanado {len(números)} valores da lista: {números} Pronto
# Somando os valores pares de {números} temos {soma}''')

    
    
# sorteia()


# Resolução do professor
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(n, end=' ', flush=True)
        sleep(0.4)
    print('PRONTO !')
    

def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista} temos {soma}')
            


numeros = list()
sorteia(numeros)
somapar(numeros)
