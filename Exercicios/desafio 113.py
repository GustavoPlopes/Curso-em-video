# def leiaint(msg):
#     while True:
#         try:
#             n = int(input(msg))
#
#         except (ValueError, TypeError):
#             print('\033[0;31mERRO: por favor, digite um número inteiro valido.\033[m')
#             continue
#         except KeyboardInterrupt:
#             print('\n\033[0;31mERRO: O usuário interrompeu o programa.\033[m')
#             return 0
#         else:
#             return n
#
#
# def leiafloat(msg):
#     while True:
#         try:
#             n = float(input(msg))
#         except (ValueError, TypeError):
#             print('\033[0;31mERRO: pro favor, digite um número do tipo real valido.\033[m')
#         except KeyboardInterrupt:
#             print('\033[0;31mERRO: O Usuário interrompeu o programa\033[m]')
#             return 0
#         else:
#             return n

from utilidadesCev import dado



n1 = dado.leiaint('Digite um número inteiro: ')
n2 = dado.leiafloat('Digite um número real: ')
print(f'\033[1;34mO valor inteiro digitado foi {n1} e o real {n2}\033[m')
