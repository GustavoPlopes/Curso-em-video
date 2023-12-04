# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 25}
#
# el pessoas['sexo']
# pessoas['nome'] = 'Leandro'
# pessoas['peso'] = 100
#
# print(pessoas)
# print(pessoas['nome'])
# print(f'O {pessoas["nome"]} tem {pessoas['idade']} anos')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
#
# for k in pessoas.keys():
#     print(k)
# for k in pessoas.values():
#     print(k)
# for k,v in pessoas.items():
#     print(f'Meu {k} é {v} ')

# brasil = []
# estado = {'uf': 'Brasília', 'sigla': 'DF'}
# estado2 = {'uf': 'São paulo', 'sigla': 'SP'}
# brasil.append(estado)
# brasil.append(estado2)
# print(brasil[1]['uf'])

brasil = list()
estado = dict()
for x in range(0, 3):
    estado['uf'] = str(input('Digite o estado: '))
    estado['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())
print(brasil)
