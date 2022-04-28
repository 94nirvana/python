'''
List Comprehension pt2

'''

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

print('-------')

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)