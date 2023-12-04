# exemplo 1
# tempo = int(input('Quantos anos tem seu carro? '))
# if tempo <= 3:
#     print('Carro novo')
# else:
#     print('Carro velho')
# print('Fim')

# exemplo 2
# tempo = int(input('Quantos anos tem seu carro? '))
# print('Carro Novo' if tempo <= 3 else 'Carro Velho')
# print('-Fim-')
# ////////////////////////////////////////////////////////////////////////////////////

# exemplo 3
# nome = str(input('Qual o seu nome? ')).strip().title()
# if nome == 'Gustavo':  # se tiver apenas o if é condição simples
#     print('Que nome lindo!')
# else:  # se tiver o else condição composta
#     print('Seu nome é tão normal!')
# print(f'Bom dia, {nome}')

# exemplo 4
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3 + n4)/4
print(f'Sua media é: {media:.1f}')
if media >= 5.0:
    print('Você alcançou a media! PARABENS, APROVADO!')
else:
    print('Você não alcançou a média! REPROVADO!')