import random
computador = random.randint(0, 10)
print(f'''{'+-' * 40}
Olá sou o computador, irei pensar em um numero de 0 a 10, tente adivinhar...
{'+-' * 40}''')
jogador = int(input('Digite o numero do seu palpite: '))
palpite = 1

while computador != jogador:
    palpite += 1
    if computador > jogador:
        print('Pensei em um numero MAIOR... Tente novamente.')
        jogador = int(input('Digite seu novo palpite: '))
    else:
        print('Pensei em um numero MENOR... Tente novamente.')
        jogador = int(input('Digite seu novo palpite: '))

print(f'Voce acertou no {palpite}º palpite')
