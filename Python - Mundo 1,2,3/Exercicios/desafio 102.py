def fatorial(n , show=False):
    """
    -> calucula o fatorial de um numero
    N = Numero que ira ser calculado
    Show = Se for True mostra a conta se False não mostra
    """
    f = 1
    if show == True:
        for c in range(n, 0, -1):
            f *= c
            print(f'{c}', end=' ' '= ' if c == 1 else ' x ')
        return f
    else:
        for c in range(n, 0, -1):
            f *= c
        return f
        
        
print(fatorial(5, False))
help(fatorial)