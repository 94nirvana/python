'''
Dictionary Comprehension

lista = [1,2,3,4]
tupla = (1,2,3,4)
conjunto = {1,2,3,4} # SET
dicionario = {'a': 1, 'b': 2, 'c': 3}
{chave:valor for valor in iteravel}
'''

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

print('---------------------------------')

numero = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in numero}
print(quadrados)

print('---------------------------------')

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

print('---------------------------------')

numeros = [1, 2, 3, 4, 5]

res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
