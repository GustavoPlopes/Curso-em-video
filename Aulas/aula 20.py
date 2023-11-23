def tit(msg):
    print('-'*30)
    print(f'{f"{msg}":^30}')
    print('-'*30)


tit('CARROS')
tit('MERCADO DO GUSTAVO')


def soma(a, b):
    s = a + b
    print(s)


soma(5, 5)
soma(15, 15)


def contador(*num):
    print(f'Recebi os valores {num} que tem {len(num)} números')


contador(8, 7, 80, 1, 3)
