# metros = float(input('Escreva em metros para transformar em centímetros e milímetros: '))
# print(f'{metros}m em centímetros é: {metros * 100}cm\nE em milímetros {metros * 1000}mm')

from time import sleep
while True:
    print(f'{"TRANSFORMADOR DE MEDIDAS":~^40}')
    m = float(input('Qual o tamanho da medida em metros que vai transformar? '))
    option = int(input('''Escolha para qual medida quer transformar
    [1] QUILÔMETRO
    [2] HECTÔMETRO
    [3] DECÂMETRO
    [4] DECÍMETRO                        [7] SAIR
    [5] CENTÍMETRO
    [6] MILÍMETRO
    Digite aqui >>>>> '''))
    if option == 1:
        quilometro = m / 1000
        print(f'Sua medida de {m}M em quilômetros é {quilometro}km')
    elif option == 2:
        hectometro = m / 100
        print(f'Sua medida de {m}M em hectômetro é {hectometro}hm')
    elif option == 3:
        decametro = m / 10
        print(f'Sua medida de {m}M em decâmetro é {decametro}dam')
    elif option == 4:
        decimetro = m * 10
        print(f'Sua medida de {m}M em decímetro é {decimetro}dm')
    elif option == 5:
        centimetros = m * 100
        print(f'Sua medida de {m}M em centímetro é {centimetros}cm')
    elif option == 6:
        milimetros = m * 1000
        print(f'Sua medida de {m}M em milímetro é {milimetros}mm')
    elif option == 7:
        break

print('Finalizando programa ...')
sleep(2)
print('Programa finalizado, volte sempre.')