'''
Map
Com map fazemos mapeamento de valores para uma funcao.
'''

import math


def area(r):
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

print('-----------')

areas = map(area, raios)
print(list(areas))
# Retorna um map object

print('-----------')

print(list(map(lambda r: math.pi * (r**2), raios)))

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26)]

c_para_f = lambda dado: (dado[0], (9 / 5 * dado[1] + 32))
print(list(map(c_para_f, cidades)))
