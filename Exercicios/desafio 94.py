dados = list()
pessoa = dict()
tot_idade = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome? ')).strip().title()
    while True:
        pessoa['Sexo'] = str(input('Sexo? [M/F]? ')).strip().upper()
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade? '))
    tot_idade += pessoa['Idade']
    dados.append(pessoa.copy())
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja adicionar os dados de outra pessoa? [S/N]? ')).strip().upper()
        if continuar not in 'SN':
            print('!ERRO! Digite apenas S ou N.')
    if continuar == 'N':
        break
print(f'{"RESULTADO":=^50}')
print(f'Foi cadastrada {len(dados)}' if len(dados) == 1 else f'Foram cadastradas {len(dados)}',
      'pessoa' if len(dados) == 1 else 'pessoas')
media = tot_idade // len(dados)
print(f'''{"-="*25}
A média de idade do grupo é de {media}
{"-="*25}''')
print('↓ Lista de mulheres cadastradas ↓')
for p in dados:
    if p['Sexo'] in 'Ff':
        print(f'>>> {p['Nome']} com {p['Idade']} anos')
print(f'{"PESSOAS COM IDADE ACIMA DA MÉDIA":=^48}')
for p in dados:
    if p['Idade'] > media:
        print(f'>>> {p['Nome']} com {p['Idade']} anos')
print('<<<ENCERRADO>>>')





