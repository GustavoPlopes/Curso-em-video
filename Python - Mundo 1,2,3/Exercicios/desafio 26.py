text = str(input('Escreva uma frase: ')).strip()
print(f'A letre "a" aparece {text.upper().count("A")} vez\nEla aparece a primeira vez na posição {text.upper().find("A")+1}\nA ultima letra a aparece na posição {text.upper().rfind("A")+1}')
