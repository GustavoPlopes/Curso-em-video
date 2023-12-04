def notas(*n, sit=False):
    """Função para analisar varias notas e a situação do aluno

    Args:
        sit (bool, optional): 

    Returns:
        dados = dict(): dicionario das notas e dados inseridos
    """
    dados = dict()
    dados['Total'] = len(n)
    dados['Maior'] = max(n)
    dados['Menor'] = min(n)
    Média = sum(n) / len(n)
    dados['Média'] = float(f'{Média:.2f}')
    if sit:
        if dados['Média'] >= 7:
            dados['Situação'] = 'Boa'
        elif dados['Média'] >= 5:
            dados['Situação'] = 'Razoavel'
        else:
            dados['Situação'] = 'Ruim'
    return dados


resp = notas(7, 4.5, 9, 7, sit=True)
print(resp)
help(notas)