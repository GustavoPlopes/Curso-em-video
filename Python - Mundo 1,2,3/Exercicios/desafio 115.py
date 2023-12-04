from utilidadesCev.cadastro import *
from utilidadesCev.cadastro.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    resposta = menu(['Cadastrar pessoa', 'Listar pessoas', 'Sair do sistema'])
    if resposta == 1:
        cabeçalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        lerarquivo(arq)
    elif resposta == 3:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('ERRO: Digite uma opção valida')
