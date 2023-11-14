import random
import time
jogador = int(input(f'''{'JOKENPO':=^40}
Escolha uma opção:
[0]- PEDRA
[1]- PAPEL
[2]- TESOURA
Digite a sua jogada: '''))
print('JO')
time.sleep(1)
print("KEN")
time.sleep(1)
print('PO')
time.sleep( 2)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

if jogador == computador:
    print(f'Computador jogou {itens[computador]}\nJogador jogou {itens[jogador]}\nDeu empate')

elif jogador != computador:
    if computador == 0:
        if jogador == 1:
            print(f'Computador jogou {itens[computador]}\nJogador jogou {itens[jogador]}\nJogador GANHOU!')
        elif jogador == 2:
            print(f'Computador jogou {itens[computador]}\nJogador jogou {itens[jogador]}\nComputador GANHOU!')
        else:
            print('Opção invalida, !TENTE NOVAMENTE!')
    elif computador == 1:
        if jogador == 0:
            print(f'Computador jogou {itens[computador]}\nJogador jogou {itens[jogador]}\nComputador GANHOU!')
        elif jogador == 2:
            print(f'Computador jogou {itens[computador]}\nJogador jogou {itens[jogador]}\nJogador GANHOU!')
        else:
            print('Opção invalida, !TENTE NOVAMENTE!')
    elif computador == 2:
        if jogador == 0:
            print(f'Computador jogou {itens[computador]}\nJogador jogou {itens[jogador]}\nJogador GANHOU!')
        elif jogador == 1:
            print(f'Computador jogou {itens[computador]}\nJogador jogou {itens[jogador]}\nComputador GANHOU!')
        else:
            print('Opção invalida, !TENTE NOVAMENTE!')
