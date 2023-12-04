def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: "{entrada}" não é um preço valido.\033[m')
        else:
            valido = True
            return float(entrada)


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


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número real valido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mERRO: Usuário encerrou o programa.\033[m')
        else:
            return n


