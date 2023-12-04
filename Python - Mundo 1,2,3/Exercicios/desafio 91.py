# from random import randint
# from time import sleep
# from operator import itemgetter
# import emoji
# print(f'''{"":=^48}
# {"SORTEIO DE DADOS":^48}
# {"":=^48}''')
# resultados = {'Jogador 1': randint(1, 6),
#               'Jogador 2': randint(1, 6),
#               'Jogador 3': randint(1, 6),
#               'Jogador 4': randint(1, 6)}
# ranking = dict()
# for k, v in resultados.items():
#     print(emoji.emojize(f'{k} jogou e o dado caiu no número {v}:game_die:....'))
#     sleep(1)
# ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
# print(f'{"RANKING":=^48}')
# for i, v in enumerate(ranking):
#     print(f'{i+1}º lugar: {v[0]} com o numero {v[1]}')
#     sleep(1)
# print(f'{"":^48}')

from random import randint
from emoji import emojize
from operator import itemgetter
from time import sleep
print(f'''{"":=^48}
{"SORTEIO DE DADOS":^48}
{"":=^48}''')
resultados = dict({'Jogador 1': randint(1, 6),
                   'Jogador 2': randint(1, 6),
                   'Jogador 3': randint(1, 6),
                   'Jogador 4': randint(1, 6)})
ranking = list()
for k, v in resultados.items():
    print(emojize(f'O {k} rolou o dado e caiu no número {v}:game_die:...'))
    sleep(1)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print(emojize(f'{"RANKING:trophy:":=^48}'))
for i, c in enumerate(ranking):
    print(emojize(f'O {i+1}:sports_medal: lugar {c[0]} com o número {c[1]}'))
    sleep(1)
