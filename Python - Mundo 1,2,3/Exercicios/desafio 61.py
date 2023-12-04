# n1 = int(input(f'''{'=' * 10}PROGRESSÃO ARITMÉTICA{'=' * 10}
# Digite o termo: '''))
# n2 = int(input('Digite a razão: '))
# termo = n1
# c = 1
#
# while c <= 10:
#     print(f'{termo}', ' ► ' if c <= 9 else 'FIM', end='')
#     termo += n2
#     c += 1


from emoji import emojize
primeiro = int(input(f'''\033[1:34m{'/-↑' * 10}PROGRESSÃO ARITMÉTICA{'/+↑' * 10}\033[m
Digite o termo: '''))
razão = int(input('Digite a razão: '))
c = 1
termo = primeiro
while c <= 10:
    print(f'\033[1:32m{termo}\033[m', ' → ' if c <= 9 else emojize(' -\033[1:4:42m FIM :partying_face:\033[m'), end='')
    termo += razão
    c += 1