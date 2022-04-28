'''
List Comprehension

- Utilizando List Comprehension nos podemos gerar novas listas com dados processados
a partir de outro iteravel.

# Sintaxe:
[ dado for dado in iteravel ]
'''

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)
print('--------------------------------')
'''
para melhor entender o que esta acontecendo devemos dividir a expressão em duas partes:
-> 1ª for numero in numeros
-> 2ª numero * 10
'''

res = [numero / 2 for numero in numeros]
print(res)

print('--------------------------------')


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)

print('--------------------------------')

num_dobrados = []
for numero in numeros:
    num_dobrado = numero * 2
    num_dobrados.append(num_dobrado)

print(num_dobrados)

print('--------------------------------')

print([numero * 2 for numero in numeros])

print('--------------------------------')

nome = 'Geek University'

print([letra.upper() for letra in nome])

print('--------------------------------')

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amigo.title() for amigo in amigos])

print('--------------------------------')

print([numero * 3 for numero in range(1, 10)])

print('--------------------------------')

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

print('--------------------------------')

print([str(numero) for numero in [1, 2, 3, 4, 5]])

print('--------------------------------')