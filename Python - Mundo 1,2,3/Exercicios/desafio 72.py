por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
               'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input(f'''{"":*^52}
Digite um numero de 1 a 20 para sabe-lo por extenso:  '''))
print(f'{"":*^52}')

while True:
    if n > 20:
        n = int(input('Numero invalido, digite novamente: '))
    else:
        break
print(f'{"":*^52}' if n <= 20 else '')
print(f'O numero {n} por extenso é {por_extenso[n]}')
