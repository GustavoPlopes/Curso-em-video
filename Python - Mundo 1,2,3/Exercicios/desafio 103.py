def ficha(nome='', gols='0'):
    if nome not in '' and gols not in '':
        print(f'O jogador {nome} fez {gols} gols.')
    elif nome not in '' and gols in '':
        print(f'O jogador {nome} fez 0 gols.')
    elif nome == '':
        if gols == '':
            print(f'O jogador desconhecido fez 0 gols.')
        else:
             print(f'O jogador desconhecido fez  {gols} gols.')
        
    
    
ficha(nome = str(input('Qual o nome do jogador? ')).strip().title, gols = str(input(f'Quantos gols fez? ')).strip())