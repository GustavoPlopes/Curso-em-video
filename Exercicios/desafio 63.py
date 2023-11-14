# n = int(input('Digite a quantidade de termos da sequencia de fibonacci que deseja ver: '))
# t1 = 0
# t2 = 1
# print(f'{t1} → {t2}',end=' → ')
# cont = 3
# while cont <= n:
#     t3 = t1 + t2
#     print(f'{t3}', end=' → ')
#     t1 = t2
#     t2 = t3
#     cont += 1
# print('FIM')

from time import sleep
n = int(input('Digite a quantidade de termos de fibonacci que deseja ver: '))
t1 = 0
t2 = 1
cont = 3
mais = n
total = 0
print(f'{t1} → {t2}', end=' → ')
while mais != 0:
    total = total + mais
    while cont <= total:
        t3 = t1 + t2
        print(f'{t3}', end=' → ')
        t1 = t2
        t2 = t3
        cont += 1
    mais = int(input('\nDigite mais quantas sequencias deseja, se quiser sair digite 0: '''))
print(f'''\033[1:34:40m{'='*38}\033[m
\033[1:34:40mNo total foram exibidos {total} termos\033[m
\033[1:34:40mFinalizando programa ...\033[m
\033[1:34:40m{'='*38}\033[m''')
sleep(4)
print('!!PROGRAMA FINALIZADO!!')