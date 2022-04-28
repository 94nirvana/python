'''
Modulo Collections - Named Tuple

são tuplas, diferenciadas, onde especificamos um nome para a mesma e tambem parametros
'''

tupla = 1, 2, 3
print(tupla[1])

from collections import namedtuple

cachorro = namedtuple('cachorro', 'idade raca nome')

cachorro2 = namedtuple('cachorro', 'idade, raca, nome')

cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

ray = cachorro(idade=2, raca='pitbull', nome='ray')
fumaca = cachorro2(idade=4, raca='pitbull', nome='fumaca')
ponta = cachorro3(idade=3, raca='pitbull', nome='ponta')
print(ray)
print('-----')
print(fumaca)
print('-----')
print(ponta)
print('-----')
print(ray[2])
print(fumaca[1])
print(ponta[0])
print('-----')
print(ray.idade)
print(fumaca.raca)
print(ponta.nome)
print('-----')