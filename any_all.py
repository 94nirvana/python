'''
Any e All

all() -> retorna True se todos os elementos do iteravel sao verdadeiros, ou, ainda se o iteravel esta vazio.
any() -> retorna True se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver vazio, retorna False.
'''

print(all([0, 1, 2, 3, 4]))
print('---------')
print(all([1, 2, 3, 4]))
print('---------')
print(all([]))
print('---------')
print(all('Roberto'))
print('---------')

nomes = ['Camila', 'Carlos', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))
print('---------')

# OBS: O all() quando retorna uma lista vazia [] ele retorna True, diferente da logica que o bool([]) retorna False.

print(any([0, 1, 2, 3, 4, 5]))
print('---------')
print(any([0, False, {}]))
print('---------')

nomes = ['Camila', 'Carlos', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes])) # Mesmo com um False ele retorna o True por conta dos outros elementos
print('---------')
print(any([num for num in [2, 4, 6, 8, 10] if num % 2 == 0]))
print('---------')
