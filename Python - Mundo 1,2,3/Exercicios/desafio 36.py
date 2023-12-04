import emoji
print(emoji.emojize(""":money_bag:\033[1:32mDigite a seguir oque é solicitado para 
saber se o seu empréstimo sera aprovado:money_bag:\033[m"""))
casa = float(input(emoji.emojize(':house:\033[1:34mDigite o valor da casa: \033[m')))
salario = float(input(emoji.emojize(':money_with_wings:\033[1:34mDigite o valor do seu salario: \033[m')))
tempo = int(input(emoji.emojize(':stopwatch:\033[1:34mDigite em quantos anos pretende pagar: \033[m')))
anos = tempo * 12
prestacao = casa / anos

if prestacao <= 0.3 * salario:
    print(f'O valor da prestação é de {prestacao:.2f} por {anos} meses')
else:
    print('Seu empréstimo foi negado')
