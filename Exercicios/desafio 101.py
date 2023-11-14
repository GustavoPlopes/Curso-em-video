def voto():
    from datetime import date
    idade = date.today().year - nascimento
    if idade < 16:
        print(f'Com {idade} anos, Voto negado')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos, Voto opcional')
    else:
        print(f'Com {idade} anos, Voto obrigatorio')
    
    
nascimento = int(input('Digite o seu ano de nascimento: '))
voto()