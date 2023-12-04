nome = str(input(
"""Escreva o seu nome para mostrar as seguintes funcionalidades, 
nome todo com letras maiusculas, com letra minusculas e quantas
letras tem o primeiro nome>>> """)).strip()
print(f'Seu nome em maiusculo: {nome.upper()}\nSeu nome em minusculo: {nome.lower()}\nQuantidade de letras ao todo {len(nome)-nome.count(" ")}\nQuantidade de letras do primeiro nome: {len(nome.split()[0])}')
