# print("Digite a largura e a altura para calcular a area e saber quantidade de tinta que ira precisar")
# altura = float(input('Digite a altura:'))
# largura = float(input('Digite a largura: '))
# area = altura * largura
# print(f'A area é: {altura * largura}m² e a quantidade de tinta que ira precisar é {area / 2}L')

option = 'S'
while option == 'S':
    altura = float(input('''\033[1:7:34:40mInsira a altura e a largura para calcular a area e saber quanto de tinta ira precisar\033[m 
\033[1:36mDigite a altura\033[m: '''))
    largura = float(input('\033[1:36mDigite a largura\033[m:'))
    area = altura * largura
    print(f'\033[1:36mA area é {area:.2f}m² e a quantidade de tinta que vai precisar é {area/2:.2f}L\033[m')
    option = str(input('\033[1:31mDeseja calcular outra vez? Se sim digite [S] se não [N] para finalizar o '
                       'programa\033[m: ')).strip().upper()

print('Programa finalizado!! Obrigado por usar...')