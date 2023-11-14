# text = str(input('Digite a frase para saber se é um palindromo: ')).strip().upper()
# palavras = text.split()
# junto = ''.join(palavras)
# inverso = ''
#
# for letra in range(len(junto)-1, -1, -1):
#     inverso += junto[letra]
# print(f'O inverso da {junto} é {inverso}')
# if inverso == junto:
#     print('É um palindromo')
# else:
#     print('Não é um palindromo')


text = str(input('Digite uma palavra ou frase para saber se é um palindromo: ')).strip().upper()
frase = text.split()
juntar = ''.join(frase)
inverso = juntar[::-1]

if inverso == juntar:
    print('É um palindromo')
else:
    print('Não é um palindromo')

