vinte_primeiros = ('Botafogo', 'Bragantino', 'Gremio', 'Palmeiras', 'CA Paranaense', 'Flamengo', 'Fortaleza',
                   'Fluminense', 'Atlético Mineiro', 'Cuiaba Esporte Clube', 'São paulo', 'internacional', 'Bahia',
                   'Cruzeiro', 'Corinthians', 'Vasco Gama', 'Santos', 'Goías', 'Coritiba', 'América')
# print(f'''{"":=^40}'
# Os primeiros 5 colocados são
# {"":=^40}''')
# for c in range(1, len(vinte_primeiros[1:6])):
#     print(f'{c}º colocado é {vinte_primeiros[c]}')
# print(f'''{"":=^40}
# Os últimos 4 colocados são
# {"":=^40}''')
# for c in range(17, len(vinte_primeiros)):
#     print(f'{c}º colocado {vinte_primeiros[c]}')
# print(f'''{"":=^40}
# Ordem alfabética dos times''')
# print(sorted(vinte_primeiros))
# print(f'''{"":=^40}
# O time cuiabá está na {vinte_primeiros.index("Cuiaba Esporte Clube")} ''')

print(f'{"":=^40}')
print(f'Os 5 primeiros times são {vinte_primeiros[0:6]}')
print(f'{"":=^40}')
print(f'Os últimos 4 colocados são {vinte_primeiros[-4:]}')
print(f'{"":=^40}')
print(f'Em ordem alfabética {sorted(vinte_primeiros)}')
print(f'{"":=^40}')
print(f'O cuiba está {vinte_primeiros.index("Cuiaba Esporte Clube")+1}º posição')
