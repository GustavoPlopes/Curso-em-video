n = int(input('Digite um numero inteiro: '))
soma = 0
c = 0
maior = 0
menor = 0
continuar = ''
while n != 0:
    c += 1
    soma += n
    continuar = str(input('Se quiser continuar digite [S] se não digite [N]: ')).strip().upper()
    if continuar == 'S':
        n = int(input('Digite um novo numero : '))
        if c == 1:
            maior = menor= n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    elif continuar == 'N':
        break
if continuar == 'N':
    print(f'A média entre todos os valores é de {soma // c} o maior valor é {maior} e o menor {menor}')