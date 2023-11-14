
print(f'\033[1:36m{"BANCO GPL":+^40}\033[m')
valor = int(input('Qual valor deseja sacar? R$'))
print(f'\033[1:36m{"":+^40}\033[m')
total = valor
cédula = 200
cont_cédulas = 0
while True:
    if total >= cédula:
        total -= cédula
        cont_cédulas += 1
    else:
        if cont_cédulas > 0:
            print(f'{cont_cédulas} notas de R${cédula:.2f}.')
        if cédula == 200:
            cédula = 100
        elif cédula == 100:
            cédula = 50
        elif cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 5
        elif cédula == 5:
            cédula = 2
        cont_cédulas = 0
        if total == 0:
            break
print('!!!Obrigado pro usar o banco GPL!!!')