import emoji
peso = float(input('''Digite o seu peso e altura para saber o \033[32mIMC\033[m
Digite o peso: '''))
altura = float(input('Agora digite a altura: '))
imc = (peso / altura ** 2)

if imc <= 18.5:
    print(f'Seu IMC é {imc:.1f} está abaixo do peso')
elif 18.5 < imc <= 25:
    print(f'Seu IMC é {imc:.1f} está com o peso ideal')
elif 25 < imc <= 30:
    print(f'Seu IMC é {imc:.1f} está com sobrepeso')
elif 30 < imc <= 40:
    print(f'Seu IMC é {imc:.1f} está com obesidade')
else:
    print(f"Seu IMC é {imc:.1f} está com obesidade mórbida")
