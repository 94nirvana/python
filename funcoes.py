'''
Funcoes:

-> Funções sao pequenos trechos de codigo que realizam determinada tarefa.
-> É possivel particionar os programas em varias funcoes.

OBS: Se voce escrever uma funcao que realiza varias tarefas dentro dela,
é bom fazer uma verificação para que a funcao seja simplificada.
'''

cores = ['verde', 'azul', 'amarelo', 'vermelho']

print(cores)    # o print é uma função built-in do python


def soma(a, b):
    return a + b


print(soma(3, 4))


def varer_lista(ex):
    for i in ex:
        print(i)


lista = [1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9, 9, 0]

varer_lista(lista)


def diz_oi(nome):
    print(f'Oi {nome}')


diz_oi('Roberto')
