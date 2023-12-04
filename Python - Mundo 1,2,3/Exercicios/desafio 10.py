# real = float(input('Escreva o valor que você tem em Real para ser convertido em Dólar: R$'))
# print(f'O valor de R${real:.2f} convertido para dólar é de US${real/4.85:.2f}\nE em euro é €${real/5.20:.2f}'
#       f'\nE em iene ¥${real/0.033:.2f} ')

while True:
    option = int(input(f'''{"CONVERSOR DE MOEDA":+^40}
    Escolha uma opção para converter o real R$
    [1] DÓLAR AMERICANO
    [2] DÓLAR AUSTRALIANO
    [3] DÓLAR CANADENSE
    [4] EURO
    [5] IENE
    [6] LIBRA ESTERLINA
    [7] FRANCO SUÍÇO
    [8] RENMINBI(YUAN)
    [9] PESO ARGENTINO
    [10] LIRA TURCA
    
    [0] SAIR DO PROGRAMA
    DIGITE AQUI A SUA OPÇÃO >>> '''))
    if option == 0:
        break
    real = float(input('Qual o valor em real? '))
    if option == 1:
        print(f'O valor de R${real:.2f} convertido em Dólar Americano é USD{real/5.08:.2f}')
    elif option == 2:
        print(f'O valor R${real:.2f} convertido em Dólar Australiano é AUD{real/3.13:.2f}')
    elif option == 3:
        print(f'O valor de R${real:.2f} convertido em Dólar Canadense é ISO{real/3.64:.2f}')
    elif option == 4:
        print(f'O valor de R${real:.2f} convertido em Euro é  €{real/5.23:.2f}')
    elif option == 5:
        print(f'O valor de R${real:.2f} em IENE  ¥ {real/0.034:.2f}')
    elif option == 6:
        print(f'O valor de R${real:.2f} convertido em Libra Esterlina é GBP{real/6.16:.2f}')
    elif option == 7:
        print(f'O valor de R${real} convertido em Franco Suíço é {real/5.62:.2f}')
    elif option == 8:
        print(f'O valor de R${real} convertido em Renminbi(Yuan) RMB{real/0.70:.2f}')
    elif option == 9:
        print(f'O valor de R${real} convertido em Peso Argentino é ARS{real/0.015:.2f}')
    elif option == 10:
        print(f'O valor de R${real} convertido em Lira Turca é TRY{real/0.18:.2f}')
    else:
        print('Opção invalida!! Por favor tente novamente')

print('Programa finalizado!! Obrigado por usar.')