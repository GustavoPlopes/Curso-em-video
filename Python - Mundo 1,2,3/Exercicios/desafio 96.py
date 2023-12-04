def area(b, h):
    a = b * h
    print(f'A área do seu terreno {b} x {h} é de {a}m²')


print(f'''Controle de terrenos
{"-" * 21}''')
area(b=float(input('Largura (m): ')), h=float(input('Comprimento (m): ')))


