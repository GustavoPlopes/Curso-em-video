import emoji
from datetime import date
ano = int(input(emoji.emojize(':man_lifting_weights:\033[1:34mDigite o ano que atleta nasceu para saber categoria:woman_lifting_weights: ')))
idade = (date.today().year - ano)

if idade <= 9:
    print(f'O atleta tem {idade}, categoria !MIRIM! ')
elif 9 < idade <= 14:
    print(f'O atleta tem {idade}, categoria !INFANTIL!')
elif 14 < idade <= 19:
    print(f'O atleta tem {idade}, categoria !JUNIOR!')
elif 19 < idade <= 20:
    print(f'O atleta tem {idade}, categoria !SÊNIOR!')
elif idade > 20:
    print(f'O atleta tem {idade}, categoria !MASTER!')
