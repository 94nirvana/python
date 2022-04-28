'''
Listas aninhadas - Multidimensionais
'''

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matrix 3x3

print(listas)
print(type(listas))

# Acesso aos dados:

print(listas[0])
print(listas[0][1])
print(listas[1][2])

for lista in listas:
    for num in lista:
        print(num)


velha = [["X" if numero % 2 == 0 else "O" for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

print([['*' for i in range(1, 4)] for j in range(1, 4)])
