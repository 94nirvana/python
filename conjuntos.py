'''
Conjuntos:
-> em qualquer linguagem de programação estamos fazendo referencia a teoria dos conjuntos da matematica.
-> em python os conjuntos sao chamados de SETs.
-> SETs não possuem duplicados, ordenados, os elementos nao sao acessados via indice, não são indexados.

Servem para:
-> Quando precisamos armazenar elemnetos, mas não nos importamos com a ordem.
-> Quando nao precisamos nos preocupar com itens duplicados.
-> Quando nao precisamos nos preocupar com as chaves.
-> Aceitam qualquer tipo de dados.

São referenciados com chaves {}
-> A diferença entre o dicionario e o conjunto é que um tem chave/valor e o outro apenas valor.
'''

s = set({0, 1, 2, 2, 3, 2, 3, 3, 4, 5, 5, 6, 7})

print(s)
print(type(s))

# Ao criar um conjunto valores ja existentes são ignorados.

# Forma mais comum:

s = {1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 6, 7, 8, 9, 0}
print(s)

# >>> Importante lembrar que além de nao duplicar valores, não existe ordem tambem <<< #

s = {99, 2, 34, 23, 12, 1, 44, 5}
print(s)

# Adicionando elementos

a = {1, 2, 3, 4}
a.add(5)
print(a)

# Remover elementos

a.remove(2)   # Usa-se o valor, não o indice.
print(a)

a.discard(1)
print(a)

a.remove(5)
print(a)

# Remover tudo:

a.clear()
print(a)

print("--------------")

conj1 = {'Roberto', 'Joao', 'Henrique', 'Patricia', 'Helena', 'Julia'}
conj2 = {'Roberto', 'Patricia', 'Helena', 'Ana', 'Clarissa'}

todos = conj1.union(conj2)
print(todos)

print("--------------")

print(conj1|conj2)

print("--------------")

ambos = conj1.intersection(conj2)
print(ambos)

print("--------------")

ambos = conj1 & conj2
print(ambos)

print("--------------")

exclusivo1 = conj1.difference(conj2)
print(exclusivo1)

print("--------------")

exclusivo2 = conj2.difference(conj1)
print(exclusivo2)

print("--------------")

# SOMA, MAX, MIN, TAMANHO

f = {1, 2, 3, 4, 5}
print(sum(f))
print(max(f))
print(min(f))
print(len(f))
