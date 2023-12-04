lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
# print(lanche)
#
# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# '''ou'''
# for cont in range(0, len(lanche)):
#     print(cont)
# ''' ou'''
for cont in range(0, len(lanche)):
    print(f'Vou come {lanche[cont]} na posição {cont}')
# '''ou'''
# for pos, comida in enumerate(lanche):
#     print(f'Vou comer {comida} na posição {pos}')
# print('Comi bastante')
#
# print(sorted(lanche))

a = 2, 5, 4
b = 5, 8, 1, 2
c = b + a
print(c.count(8))
#
a = 2, 5, 4
b = 5, 8, 1, 2
c = b + a
print(c.index(8))