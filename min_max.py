'''
Min e Max

max() -> retorna o maior valor de um iteravel ou o maior de dois ou mais elementos.

'''

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))
print('--------')
print(min(lista))
print('--------')
tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))
print('--------')
print(min(tupla))
print('--------')
conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))
print('--------')
print(min(conjunto))
print('--------')
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))
print('--------')
print(min(dicionario.values()))
print('--------')

val1 = int(input("Digite um valor: "))
val2 = int(input("Digite um valor: "))
print(max(val1, val2))
print('--------')
print(min(val1, val2))
print('--------')

print(max(4, 54, 67, 89, 43, 12))
print('--------')
print(max('a', 'b', 'c'))
print('--------')
print(min('a', 'b', 'c'))
print('--------')
print(max('a', 'ab', 'abc'))
print('--------')
print(min('a', 'ab', 'abc'))
print('--------')
print(min("GeekUniversity"))
print('--------')


nomes = ['Arya', 'Samsa', 'Dora', 'Tim', 'Olavo']

print(max(nomes))   # Leva em consideração a ordem alfabetica
print('--------')
print(min(nomes))   # Leva em consideração a ordem alfabetica
print('--------')
print(max(nomes, key=lambda nome: len(nome)))
print('--------')
print(min(nomes, key=lambda nome: len(nome)))
print('--------')