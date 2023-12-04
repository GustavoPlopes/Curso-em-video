try:
    name = str(input('Qual seu nome? ')).strip()
    a = int(input('Digite o numerador da divisão: '))
    b = int(input('Digite o denominador da divisão: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos problemas com o tipo de dados digitados')
except ZeroDivisionError:
    print('o denominador não aceita o número "0"')
except KeyboardInterrupt:
    print('O usuário preferiu não informar todos os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'{a} / por {b} = {r:.1f}')
finally:
    print(f'>>Obrigado por usar o programa {name}<<')