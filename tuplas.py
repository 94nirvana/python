'''
Tuplas (tuple)

São bem parecidas com listas, exitem apenas algumas diferenças:
- representadas por ()
- são imutaveis, não mudam, toda operação gera uma nova tupla.
- sao definidas pela virgula mais que pelo uso dos parenteses
'''

tupla1 = (1,2,3,4,5,6)
print(tupla1)

print(type(tupla1))

tupla2 = 1,2,3,4,5,6
print(tupla2)

print(type(tupla2))

tupla3 = (3,)
print(tupla3)

print(type(tupla3))

print('---------------')

tupla = ('Geek', 'University')

elem1, elem2 = tupla

print(elem1)
print(elem2)


print('------------')
'''
Nao EXISTEM METODOS DE ADICAO E REMOCAO, SAO IMUTAVEIS.
'''

'''
Para valores reais
soma -> print(sum(tupla))
max -> print(max(tupla))
min -> print(min(tupla))
len -> print(len(tupla))
'''

tupla1 = 1,2,3
tupla2 = 4,5,6
tupla3 = tupla1 + tupla2
print(tupla3)

print('------------')

for i in tupla3:
    print(i)

print('------------')

'''
Devemos utilizar tuplas sempre que nao precisarmos modificar os dados contidos em uma coleção.
ex.: meses = ('jan','fev','mar'....)

Acesso ao elementos igual as listas atraves dos indices.
'''
i=0
while i<len(tupla3):
    print(i)
    i += 1

print('------------')

print(tupla3.index(2))

