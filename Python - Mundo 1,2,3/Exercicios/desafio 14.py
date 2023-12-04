# fahrenheit = float(input('Escreva em graus fahrenheit para ser convertido em celsius: '))
# print(f'A conversão de {fahrenheit}F para celsius é {(fahrenheit - 32) * 5/9:.2f}C')
#
# celsius = float(input('Escreva em graus celsius para ser convertido em fahrenheit: '))
# print(f'A conversão de {celsius:.2f}C para fahrenheit é {celsius * 1.8 + 32:.2f}')

print(f'''{"":=^48}
{"CALCULADORA DE CONVERSÃO DE TEMPERATURA":^48}
{"":=^48}''')
lista = []
graus = []
while True:
    opção = str(input('Digite [C] para transformar celsius em fahrenheit ou [F] par transformar fahrenheit '
                      'em celsius:  ')).strip().upper()
    if opção == 'C':
        nome = str(input('Qual seu nome? '))
        lista.append(nome)
        celsius = float(input('Digite a temperatura em graus celsius, para ser transformada em graus fahrenheit: '))
        fah = celsius * 1.8 + 32
        lista.append(fah)
        f = 'graus fahrenheit'
        graus.append(f)
        print(f'''{celsius:.2f}º graus celsius em fahrenheit é {fah:.2f}º graus''')
    elif opção == 'F':
        nome = str(input('Qual seu nome? '))
        lista.append(nome)
        fahrenheit = float(input('Digite a temperatura em graus fahrenheit para ser transformada em graus celsius: '))
        cel = (fahrenheit - 32) * 5/9
        lista.append(cel)
        c = 'graus celsius'
        graus.append(c)
        print(f'{fahrenheit:.2f}º graus fahrenheit em celsius é {cel:.2f} ')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        print(f'{"":=^48}')
    if continuar == 'N':
        break
print(f'''{"LISTA DAS TEMPERATURAS":^48}
{"":=^48}''')
for l in range(0, len(lista)):
    if l % 2 == 0:
        print(f'A temperatura  do {lista[l]} é ', end='')
    else:
        print(f'{lista[l]:.2f}º ', end='')
        for g in range(0, len(graus)):
            if g % 2 == 0:
                print(f'{graus[g]}')
            else:
                print(f'{graus[g]}')

