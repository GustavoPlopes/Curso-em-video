# palavras = ('gratis', 'amor', 'palavra', 'ar-condicionado', 'mesa', 'cadeira', 'teclado',
#            'controle', 'boneco')


# for p in palavras:
#    print(f'\nA palavra {p} tem as vogais, ', end='')
#    for letra in p:
#        if letra.lower() in 'aeiou':
#            print(letra, end=' ')


print(f'''{"":=^48}
{"DIGITE PALAVRAS PARA SABER SUAS VOGAIS":^48}
{"":=^48}''')
while True:
    palavras = (str(input('1º palavra: ')), str(input('2º palavra: ')),
                str(input('3º palavra: ')), str(input('4º palavra: ')), str(input('5º palavra: ')))
    print(f'{"":-^48}')
    for p in palavras:
        print(f'A palavra {p} tem as vogais, ', end='')
        for vogais in p:
            if vogais.lower() in 'aáàâãeéèêiíìîoóòõôuúùû':
                print(f'{vogais}\n', end='')
    print(f'{"":-^48}')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        print(f'{"":-^48}')
    if continuar == 'N':
        break

print(f'''{"":-^48}
Obrigado por usar o programa!!''')