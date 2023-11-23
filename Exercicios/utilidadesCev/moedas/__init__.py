def metade(n, form=False):
    if form:
        return moeda(n / 2)
    else:
        return n / 2


def dobro(n, form=False):
    if form:
        return moeda(n * 2)
    else:
        return n * 2


def aumento(n, porcen, form=False):
    tot = porcen * n / 100
    if form:
        return moeda(n + tot)
    else:
        return n + tot


def reduzindo(n, porcen, form=False):
    tot = porcen * n / 100
    if form:
        return moeda(n - tot)
    else:
        return n - tot


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(n, porcen1=0, porcen2=0):
    print(f'''{"~"*30}
{"RESUMO DO VALOR":^30}
{"~"*25}
Preço analisado:  \t{moeda(n)}
Dobro do preço:  \t{moeda(dobro(n))}
Metade do preço:  \t{moeda(metade(n))}
{porcen1}% de aumento:  \t{moeda(aumento(n, porcen1))}
{porcen2}% de redução:  \t{moeda(reduzindo(n, porcen2))}
{"~"*30}
''')
