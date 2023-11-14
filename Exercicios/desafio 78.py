# valores = list()
# maior_valor = 0
# menor_valor = 0
# print(f'''{"":-^80}
# {"DIGITE 4 NUMEROS PARA SABER QUAL O MENOR, MAIOR E EM QUAL POSIÇAO ESTÁ":^80}
# {"":-^80}''')
# for v in range(0, 5):
#     valores.append(int(input(f'{v+1}º valor :')))
#     if v == 0:
#         maior_valor = menor_valor = valores[v]
#     else:
#         if valores[v] > maior_valor:
#             maior_valor = valores[v]
#         if valores[v] < menor_valor:
#             menor_valor = valores[v]


# print(f'''{"":=^48}
# O maior valor digitado é {maior_valor} e está na {valores.index(maior_valor)+1}º posição
# O menor valor digitado é {menor_valor} e está na {valores.index(menor_valor)+1}º posição
# {"":=^48}''')

valor = []
maior = menor = 0
for v in range(0, 5):
    valor.append(int(input(f'{v+1}º Valor: ')))
    if v == 0:
        maior = menor = valor[v]
    else:
        if valor[v] > maior:
            maior = valor[v]
        if valor[v] < menor:
            menor = valor[v]
print(f'''
O maior valor é {maior} e está na {valor.index(maior)+1}º posição
O menor valor é {menor} e está na {valor.index(menor)+1}º posição''')

