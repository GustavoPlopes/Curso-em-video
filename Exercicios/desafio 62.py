termo = int(input('\033[1:30:45mDigite o termo\033[m: '))
razão = int(input('\033[1:30:45mDigite a razão\033[m: '))
c = 1
t = termo
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        print(f'\033[1:34m{t}\033[m', end=' - ')
        c += 1
        t += razão
    print('\033[1:32mPAUSA\033[m')
    mais = int(input('\033[1:30:45mDigite mais quantas progressões você quer ver\033[m: '))
print(f'\033[1:30:44mNo total foram \033[1:31m{total}\033[1:30:44m progressões\033[m')