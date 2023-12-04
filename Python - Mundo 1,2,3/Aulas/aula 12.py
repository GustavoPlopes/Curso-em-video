# condição simples
# nome = str(input('Qual seu nome? ')).title()
# if nome == 'Gustavo':
#     print('Que nome bonito!')
# print(f'Tenha um bom dia {nome}')

# condição composta
nome = str(input('Qual seu nome? ')).title()
if nome == 'Gustavo':
    print(f'Que nome bonito')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é bem popular no brasil')
else:
    print('Seu nome é bem normal')
