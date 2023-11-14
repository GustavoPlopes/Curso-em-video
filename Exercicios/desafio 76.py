tabela = ('Frango', 7.33,
          'Bolacha', 3.5,
          'Pão', 0.80,
          'Macarrão',7.80,
          'Oléo', 3.75,
          'Caqui', 8.00,
          'Arroz', 12.00,
          'Mandioca', 1.50)

# print(f'''{"":-^45}
# {"LISTAGEM DE PREÇOS":^45}
# {"":-^45}
# {tabela[0]}...........................R$ {tabela[1]}
# {tabela[2]}...........................R$ {tabela[3]}0
# {tabela[4]}...........................R$ {tabela[5]}0
# {tabela[6]}...........................R$ {tabela[7]}0
# {tabela[8]}...........................R$ {tabela[9]}
# {tabela[10]}...........................R$ {tabela[11]}0
# {tabela[12]}...........................R$ {tabela[13]}0
# {tabela[14]}...........................R$ {tabela[15]}0
# {"":-^45}
# ''')

print(f'''{"":-^45}
{"LISTAGEM DE PREÇOS":^45}
{"":-^45}''')
for n in range(0, len(tabela)):
    if n % 2 == 0:
        print(f'{tabela[n]:.<30}', end='')
    else:
        print(f'{tabela[n]:>7.2f}')
print(f'{"":-^45}')