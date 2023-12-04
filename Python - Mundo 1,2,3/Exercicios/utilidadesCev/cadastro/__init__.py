def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO: Usuário encerrou o programa')
        else:
            return n


def cabeçalho(txt):
    print(f'''{"~"*42}
{txt.center(42)}
{"~"*42}''')


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    opc = leiaint('Sua opção: ')
    return opc


