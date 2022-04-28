"""
Funcoes com paramentros:

- Funcoes que recebem dados para serem processados dentro da mesma.
"""


def quadrado(num):
    return num ** 2


print(quadrado(9))
print(quadrado(8))
print(quadrado(6))
print('---------')


def cantar_parabens(nome):
    return f'Parabens pra voce\nNessa data querida\nMuitas felicidades\nMuitos anos de vida\nViva o {nome}'


print(cantar_parabens("Roberto"))
print('---------')


def pessoa(nome, idade, valor):
    return f'{nome}, tem {idade} anos, e {valor} no banco!'


print(pessoa("Roberto", 33, 1500))
print('---------')





