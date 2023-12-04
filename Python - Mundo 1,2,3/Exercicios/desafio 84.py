lista = list()
pessoas = list()
pessoa_pesada = pessoa_leve = ''
pesadas = leve = 0
while True:
    lista.append(str(input('Digite seu nome: ')))
    lista.append(float(input('Digite a seu peso: ')))
    if len(pessoas) == 0:
        pesadas = leve = lista[1]
        pessoa_pesada = pessoa_leve = lista[0]
    else:
        if lista[1] > pesadas:
            pesadas = lista[1]
        if lista[1] < leve:
            leve = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]? ')).strip().upper()
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')

print(f'O maior peso foi {pesadas:.2f}Kg, e está cadastrado no nome de ', end=' ')
for p in pessoas:
    if p[1] == pesadas:
        print(f'{p[0]}, ', end='Fim' if pessoas[-1] else '')
print(f'\nO menor peso foi {leve:.2f}Kg, e está cadastrado no nome de ', end='')
for p in pessoas:
    if p[1] == leve:
        print(f'{p[0]} ', end='')
