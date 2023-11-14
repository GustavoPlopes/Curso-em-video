n = 0

while True:
    print(f'{"="*42}')
    n = int(input(f'Digite um valor para saber a sua tabuada ou um numero negativo como [-1] para finalizar o programa: '))
    print(f'{"="*42}')
    if n < 0:
        break
    for x in range(1, 11):
        tabuada = n * x
        print(f'{n} x {x} = {tabuada}')
print('Finalizado')