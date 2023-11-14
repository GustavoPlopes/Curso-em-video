# import random
# num = int(input('Tente adivinhar qual numero o computador pensou de 0 a 5: '))
# mist = range(6)
# if random.choice(mist) == num:
#     print('Parabéns, você venceu!')
# else:
#     print(f'Que pena, você perdeu, eu pensei no numero {mist} e você no {num}!')

# Versão do professor
from random import randint
from time import sleep
import emoji
computador = randint(0,5)
print('-=-' * 20)
print(emoji.emojize(':game_die:Vou pensar em um numero entre 0 a 5. Tente adivinhar ...:game_die:'))
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('AGUARDE PROCESSANDO...')
sleep(2)
if jogador == computador:
    print(emoji.emojize(f'Parabens !:partying_face:!:partying_face: você acertou, nós pensamos igualmente no numero {computador}'))
else:
    print(emoji.emojize(f'Que pena, você errou!:persevering_face: eu pensei no numero {computador} e você no {jogador}'))

