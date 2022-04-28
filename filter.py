'''
Filter
filter() -> Serve para filtrar dados de uma determinada coleção.
'''

import statistics

# Dados coletados de algum sensor:

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#Calculando a media -> mean()

media = statistics.mean(dados)

# Assim como a funcao map, a filter recebe dois parametros, sendo uma funcao e um iteravel.

res = filter(lambda x: x > media, dados)
print(list(res))

# Assim como na funcao map os dados nao ficam salvos na memoria, apos o uso.

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje!']},
    {'username': 'gal', 'tweets': []}
]

print(usuarios)
print('---------------------------------------------------------')
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)
print('---------------------------------------------------------')
inativos = list(filter(lambda u: not u['tweets'], usuarios))
print(inativos)
print('---------------------------------------------------------')
# Combinar filter e map

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo sua instrutora é + nome da instrutora, desde que cada nome tenha menos de 5 caracteres.

instrutor = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(instrutor)
print('---------------------------------------------------------')
