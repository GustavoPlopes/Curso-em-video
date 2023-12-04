print(f'''{"":=^48}
{"VALIDE UMA EXPRESSÃO":^48}
{"":=^48}''')
expr = str(input('Digite a expressão: '))
p = []
for simb in expr:
    if simb == '(':
        p.append('(')
    elif simb == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('Expressão valida...')
else:
    print('Expressão invalida...')
