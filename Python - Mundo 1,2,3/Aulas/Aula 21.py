# def somar(a=0, b=0, c=0):
#     """Soma os três valores e exibe o resultado

#     Args:
#         a (_type_): Primeiro valor
#         b (_type_): Segundo valor
#         c (_type_): Terceiro valor
        
#         s (_type_): Resultado
#     """
#     s = a + b+ c
#     print(f'A soma de {a} + {b} + {c} = {s}')
#     return s
    

# somar(1, 1, 1)
# help(somar)
# r1 = somar(9,5)
# r2 = somar(5)
# r3 = somar(1, 2 , 3)
# print(f'O resultado das somar são: {r1}, {r2}, {r3}')

# def teste(b):
#     global n
#     x = 8 # Escopo local 
#     b +=1
#     n = 5
#     print(f'Na função teste, n vale {n}')
#     print(f'Na função teste, b vale {b}')
#     print(f'Na função teste, x vale {x}')
    


# n = 2 # Escopo global
# print(f'No programa principal, n vale {n}')
# teste(n)


def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')