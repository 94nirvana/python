'''
Sorted

obs: Nao confunda com a funcao sort() que ja estudamos em listas, o sort so funciona em listas.
Podemos utilizar o sorted() com qualquer iteravel.

Como o proprio nome diz, sorted() serve para ordenar.
'''

numeros = (2, 3, 1, 2, 3, 4, 1, 5, 6)
print(sorted(numeros))
print('------------')
numeros2 = {2, 3, 1, 2, 3, 4, 1, 5, 6}
print(sorted(numeros2))
print('------------')
print(sorted(numeros, reverse=True))
print('------------')
print(sorted(numeros2, reverse=True))
print('------------')
usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': [], 'cor': 'amarelo'},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje!']},
    {'username': 'gal', 'tweets': [], 'cor': 'azul', 'musica': 'rock'}
]

print(usuarios)
print('------------')
print(sorted(usuarios, key=lambda usuario: usuario['username']))
print('------------')
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))
print('------------')

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dumb', 'tocou': 2},
    {'titulo': 'Black in Black', 'tocou': 6},
    {'titulo': 'Polly', 'tocou': 9},
]

print(sorted(musicas, key=lambda musica: musica['tocou']))
print('------------')
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))