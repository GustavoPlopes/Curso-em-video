import emoji
from datetime import date
nascimento = int(input(emoji.emojize(":calendar:Digite o seu ano de nascimento para saber sobre seu \033[1:32malistamento\033[m :right_arrow: ")))
idade = date.today().year - nascimento
if idade < 18:
    print(f"\033[34mAguarde você tem {idade} anos, falta {18 - idade} para se alistar")
elif idade == 18:
    print(f'\033[32mVocê tem 18 anos, chegou a hora de se alistar, procure uma junta militar para mais informações')
elif idade > 18:
    print(f'\033[31mVocê passou {idade - 18} anos da hora de se alistar, procure uma junta militar urgente')