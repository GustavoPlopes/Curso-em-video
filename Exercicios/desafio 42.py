import emoji
r1 = float(input(emoji.emojize('''\033[4:35mDigite as três retas para saber se forma um triangulo,
e qual tipo, se é equilátero, isóscele ou escaleno.\033[m
\033[34mPrimeiro segmento: ''')))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
total = r1 + r2 + r3
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r1 == r3:
        print('É um triangulo Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É um triangulo Isósceles')
    else:
        print('É um triangulo Escaleno')
else:
    print('Não é um triangulo')
