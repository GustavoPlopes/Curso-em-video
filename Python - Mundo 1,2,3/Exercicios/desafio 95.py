# dados = list()
# gols = list()
# jogador = dict()
# while True:
#     jogador.clear()
#     gols.clear()
#     jogador['Nome'] = str(input('Nome do jogador? ')).strip().title()
#     jogador['Partidas'] = int(input(f'Quantas Partidas {jogador['Nome']} jogou? '))
#     for p in range(0, jogador['Partidas']):
#         gols.append(int(input(f'{p+1}º partida: ')))
#     jogador['Gols'] = gols[:]
#     dados.append(jogador.copy())
#     continuar = ' '
#     while continuar not in 'SN':
#         continuar = str(input('Deseja adicionar dados de outro jogador? [S/N]? ')).strip().upper()
#         if continuar not in 'SN':
#             print('!ERRO! Digite apenas S ou N.')
#     if continuar == 'N':
#         break
# print(f'{"-="*25}')
# print('Cod', end=' ')
# for i in jogador.keys():
#     print(f'{i:<15}', end='')
# print()
# print(f'{"-"*40}')
# for k, v in enumerate(dados):
#     print(f'{k+1:>3}', end=' ')
#     for d in v.values():
#         print(f'{str(d):<15}', end='')
#     print()
# while True:
#     busca = int(input(f'''{"-="*25}
# Digite o cod para mostrar levantamento do jogador ou (999) para finalizar o programa: ''')) - 1
#     if busca == 998:
#         break
#     if busca >= len(dados):
#         print('!ERRO! Digite um cod de jogador valido.')
#     else:
#         print(f'{f"Levantamento do jogador {dados[busca]['Nome']}":-^48}')
#         for i, g in enumerate(dados[busca]['Gols']):
#             print(f'No jogo {i+1} fez {g} gols')
# print('<<<VOLTE SEMPRE>>>')


dados = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    gols.clear()
    jogador['Nome'] = str(input('Nome do jogador? ')).strip().title()
    jogador['Partidas'] = int(input(f'Quantas partidas jogou? '))
    print(f'{"DIGITE GOLS FEITOS":-^50}')
    for c in range(0, jogador['Partidas']):
        gols.append(int(input(f'{c+1}º partida: ')))
    jogador['Gols'] = gols[:]
    dados.append(jogador.copy())
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja adicionar dados de outro jogador? [S/N]? ')).strip().upper()
        print(f'{"-"*50}')
        if continuar not in 'SN':
            print('!ERRO! Digite apenas S ou N.')
    if continuar == 'N':
        break
print('Cod', end=' ')
for i in jogador.keys():
    print(f'{i:<13}', end=' ')
print()
for i, v in enumerate(dados):
    print(f'{i+1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<14}', end='')
    print()
while True:
    busca = int(input(f'''{"-"*50}
Digite o cod do jogador para ver o levantamento ou (999) para finalizar o programa: ''')) - 1
    if busca == 998:
        break
    if busca >= len(dados):
        print('!ERRO! Digite um código de jogador valido.')
    else:
        print(f'{f"Levantamento do jogador {dados[busca]['Nome']}":-^50}')
        for i, v in enumerate(dados[busca]['Gols']):
            print(f'No jogo {i+1} fez {v}')
print('<<<OBRIGADO POR USAR O PROGRAMA>>>')
