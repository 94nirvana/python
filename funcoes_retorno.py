'''
Funcoes com retorno
Return:
OBS:- Ela finaliza, sai da execução da funcao.
    - Podemos ter, em uma funcao, diferentes returns
    - Podemos retornar qualquuer tipo de dado.
'''


def quadrado(num):
    return num ** 2


print(quadrado(9))

print("-----------")


def diz_oi():
    print('Antes do retorno')
    return 'Oi'
    print('Apos return')


diz_oi()

print("-----------")


def nova():
    variavel = False  # True / None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova())

print("-----------")


def outra_func():
    return 2, 3, 4, 5


num2, num3, num4, num5 = outra_func()
print(num2, num3, num4, num5)
print(type(outra_func()))
print("-----------")

from random import random, randint


def moeda():
    valor = random()
    if valor > 0.5:
        return 'cara'
    else:
        return 'coroa'


print(moeda())
print("------------")


def mega_sena():
    valores = []
    for i in range(6):
        valores.append(randint(1, 60))
    return valores


print(mega_sena())
print("------------")


def par_impar():
    valor = randint(1, 100)
    if valor % 2 == 0:
        return 'PAR'
    return 'IMPAR'


print(par_impar())
