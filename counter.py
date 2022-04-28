'''
Modulo Collections - Counter (Contador)

Collections -> High-performace Conteiner Datatypes

Counter -> Recebe um iteravel como parametro e cria um objeto do tipo collections counter, que é parecido como dicionario, que tem como
chave o elemento da lista, e valor a quantidade de ocorrencia desse elemento.
'''

from collections import Counter


lista = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 7, 8, 9, 9, 0, 0, 0]

res = Counter(lista)

print(res)
print("------------------")
print(type(res))
print("------------------")
# para cada elemento da lista, o counter criou uma chave e colocou como valor as ocorrencias.

print(Counter("Geek University"))

print("------------------")

texto = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
           Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
           when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
           It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
           It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
           and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

palavras = texto.split()
print(palavras)
print("------------------")
print(Counter(palavras))
print("------------------")
