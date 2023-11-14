# from random import randint
# mega = list()
# dados = list()
# print(f'''{"":|^48}
# {"GERADOR DE JOGOS DA MEGA SENA":^48}
# {"":|^48}''')
# qtd = int(input('Digite quantos jogos deseja gerar: '))
# tot = 1
# while tot <= qtd:
#     cont = 0
#     while True:
#         num = randint(1, 60)
#         if num not in dados:
#             dados.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     dados.sort()
#     mega.append(dados[:])
#     dados.clear()
#     tot += 1
# print(f'{"":|^48}')
# for i, m in enumerate(mega):
#     print(f'Jogo {i+1}: {m}')
# print(f'{"BOA SORTE":|^48}')

from random import randint
from time import sleep
mega = list()
dados = list()
tot = 1
print(f'''{"":/^48}
{"GERADOR DE JOGOS DA MEGA SENA":^48}
{"":/^48}''')
qtd = int(input('Quantos jogos deseja gerar? '))
while tot <= qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in dados:
            dados.append(num)
            cont += 1
        if cont >= 6:
            break
    dados.sort()
    mega.append(dados[:])
    dados.clear()
    tot += 1
print(f'{"GERANDO JOGOS":/^48}')
for i, m in enumerate(mega):
    print(f'Jogo {i+1}: {m}')
    sleep(1)
print(f'{"BOA SORTE":/^48}')
