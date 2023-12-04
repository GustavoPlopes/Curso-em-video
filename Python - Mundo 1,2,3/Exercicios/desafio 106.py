def ajuda():
    while True:
        print(f'''\033[1;30;42m{"~"*40}
{"SISTEMA DE AJUDA PyHELP":^40}
{"~"*40}\033[m''')
        fb = str(input('Função ou Biblioteca > '))
        if fb == 'fim':
            print(f'''\033[1;30;41m{"~"*10}
{"ATÉ LOGO":^10}
{"~"*10}\033[m''')
            break
        print(f'''\033[1;30;46m{"~"*40}
{f"ACESSANDO MANUAL DO COMANDO {fb}":^40}
{"~"*40}\033[m''')
        help(fb)
        
        
ajuda()
        