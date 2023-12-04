# valor = []

# while True:
#     valor.sort()
#     n = (int(input('Digite um valor: ')))
#     if n not in valor:
#         valor.append(n)
#         print('Valor adicionado com sucesso....')
#     else:
#         print('Valor já existe na lista....')
    
#     continuar = ' '
#     while continuar not in 'SN':
#         continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
#     if continuar == 'N':
#         break
# print('Os numeros digitados foram, ', end='')
# for v in valor:
#     print(f'{v}', end=' ')

valor = []

while True:
    valor.sort()
    num = int(input(f'''{"":=^48}
{"NUMEROS EM ORDEM CRESCENTE":^48}
{"":=^48} 
Digite um valor para ser adicionado a lista: '''))
    if num not in valor:
        valor.append(num)
        print('\033[1:32mValor adicionado a lista...\033[m')
    else:
        print('\033[1:31mvalor repitido, adicione outro\033[m')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja dicionar outro numero? [S|N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'''{"":=^48}
Os valores da lista são, ''', end='')
for v in valor:
    print(v, end=' ' )