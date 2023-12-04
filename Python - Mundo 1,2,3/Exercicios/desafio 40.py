import emoji
import time
n1 = float(input(emoji.emojize(':memo:\033[1:4:35mOlá, para saber a nota da sua media\033[m:memo:\n:sparkle:\033[1:34mDigite a nota do primeiro bimestre:sparkle::')))
n2 = float(input(emoji.emojize(':sparkle:Digite a nota do segundo bimestre:sparkle:: ')))
n3 = float(input(emoji.emojize(':sparkle:Digite a nota do terceiro bimestre:sparkle:: ')))
n4 = float(input(emoji.emojize(':sparkle:Digite a nota do quarto bimestre::sparkle:\033[m ')))
media = (n1 + n2 + n3 + n4) / 4
print('Calculando...')
time.sleep(2)
if media < 5.0:
    print(emoji.emojize(f'Você tirou a média de \033[1:31m{media:.1f} !REPROVADO!\033[m:cross_mark:'))
elif media >= 5.0 and media <= 6.9:
    print(emoji.emojize(f'Você tirou a média de \033[1:33m{media:.1f} !RECUPERAÇÃO!\033[m:double_exclamation_mark:'))
elif media >= 7.0:
    print(emoji.emojize(f'Você tirou a média de \033[1:32m{media:.1f} !APROVADO!\033[m:check_mark_button: '))