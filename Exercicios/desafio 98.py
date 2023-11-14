from time import sleep


def contador(i, f, p):
    """
    The function "contador" prints a sequence of numbers from a starting point to an ending point with a
    given step size.
    
    :param i: The starting value of the counter
    :param f: The parameter "f" represents the final value of the counter
    :param p: The parameter "p" represents the step or increment value for the counter. It determines
    how much the counter will increase or decrease with each iteration
    """
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'''{"-="*20}
O contador vai de {i} até {f} de {p} em {p}.''')
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            sleep(0.5)
            cont -= p
        print('FIM')
# The code is defining a function called `contador` that takes three arguments: `i`, `f`, and `p`.
contador(1, 10, 1)
contador(10, 1, 2)
contador(i=int(input(f'''{"-="*20}
Agora personalize sua contagem
Inicio: ''')), f=int(input('Fim: ')), p=int(input('Passo: ')))



