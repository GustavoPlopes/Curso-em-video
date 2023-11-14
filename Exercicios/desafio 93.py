


aproveitamento = dict()
gols = list()
aproveitamento['Nome'] = str(input('Nome do jogador? ')).strip().title()
aproveitamento['Partidas'] = int(input('Quantidade de partidas jogadas? '))
for c in range(0, aproveitamento['Partidas']):
    gols.append(int(input(f'{c+1}º partida:  ')))
total = sum(gols)
aproveitamento['Total'] = total
aproveitamento['Gols'] = gols
print(f'''{"-="*25}
{aproveitamento}
{"-="*25}''')
for k, v in aproveitamento.items():
    print(f'O item {k} tem o valor {v}')
print(f'{"-="*25}')
print(f'O jogador {aproveitamento['Nome']} jogou {aproveitamento['Partidas']} partidas.')
for i, v in enumerate(aproveitamento['Gols']):
    print(f'Na {i+1}º partida, fez {v} gols')
print(f'O total de gols foram {aproveitamento['Total']}')






