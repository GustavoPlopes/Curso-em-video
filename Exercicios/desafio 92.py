from datetime import datetime
print(f'''{"-=" * 24}
{"IDADE DE APOSENTADORIA":^48}
{"-=" * 24}''')
dados = dict()
dados['Nome'] = str(input('Nome: ')).strip().title()
ano = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - ano
dados['ctps'] = int(input('Carteira de trabalho, se naõ tiver digite 0: '))

if dados['ctps'] == 0:
    for k, v in dados.items():
        print(f'{k} tem o valor de {v}')
else:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Contratação'] - ano + 35
    print(f'{'-=' * 48}')
    for k, v in dados.items():
        print(f'{k} tem o valor de {v}')
