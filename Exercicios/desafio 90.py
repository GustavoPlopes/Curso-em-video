aluno = dict()
aluno['nome'] = str(input('Nome do aluno(a): ')).strip().title()
aluno['média'] = float(input(f'Média do(a) {aluno['nome']}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

print(f'O aluno(a) {aluno['nome']} teve a média de {aluno['média']} e a situação é {aluno['situação']}')
for k, v in aluno.items():
    print(f'{k} é igual a {v}')