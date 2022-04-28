'''
Utilizando Lambdas
-> Conhecidas por Expressoes Lambdas, ou simplismente Lambdas, são funcoes sem nome, ou seja,
funcoes anonimas.
'''

# Ex.:

calc = lambda x: 3 * x + 1
print(calc(4))

print("--------")

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('roberto', 'prado'))

print('--------')

um = lambda x: 3 * x + 1
dois = lambda x, y: (x*y)**0.5
tres = lambda x, y, z: 3 / (1 / x+1 / y+1 / z)

print(um(9))
print(dois(9,3))
print(tres(9, 3, 6))

print('--------')

'''
Funcao Quadratica
f(x) = a * x ** 2 + b * x + c
'''


def quadratica(a,b,c):
    return lambda x: a * x ** 2 + b * x + c


teste = quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
