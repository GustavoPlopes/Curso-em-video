# sexo = str(input('Digite M para masculino e F para feminino: ')).strip().upper()[0]
# while sexo not in 'MF':
#     sexo = str(input('Digite novamente uma opção valida: ')).strip().upper()[0]
# print(f'Sexo {sexo} registrado com sucesso.')


sexo = str(input('Digite M para masculino e F para feminino: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Digite novamente uma opção valida: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso.')