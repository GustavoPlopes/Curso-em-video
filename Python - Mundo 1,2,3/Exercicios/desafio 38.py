import emoji
n1 = int(input(emoji.emojize('Digite dois valores para saber se são \033[1:31miguais\033[m ou \033[1:32mmaior\033[m\n:yellow_circle:\033[1:34mPrimeiro numero\033[m: ')))
n2 = int((input(emoji.emojize(':yellow_circle:\033[1:34mSegundo numero\033[m: '))))
if n1 == n2:
    print(emoji.emojize(f':check_mark_button:Os dois numeros, {n1} e {n2} são iguais'))
elif n1 > n2:
    print(emoji.emojize(f':check_mark_button:O primeiro numero {n1} é maior que o segundo {n2}'))
elif n2 > n1:
    print(emoji.emojize(f':check_mark_button:O segundo numero {n2} é maior que o primeiro {n1}'))
