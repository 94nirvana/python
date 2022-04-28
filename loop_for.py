'''
Utilazado para iterar sobre sequencia ou valores iteraveis(ex.:strings)
Quando usado o enumerate o for cria uma tupla com indice e valor do iteravel.
'''

palavra = "autocomplete"
for i in palavra:
    print(i)

print("--------------------")

lista = ['maca', 'banana', 'morango', 'uva', 'pera', 'amora']
for i in lista:
    print(i)

print("--------------------")

for i in range(11):
    if i % 2 == 0:
        print(i, "numero par")
    else:
        print(i, "numero impar")

print("--------------------")

qtd = int(input("Digite o numero de vezes que o loop deve rodar: "))
for i in range(qtd):
    print(i)

print("--------------------")

#Tabuada
for i in range(10):
    for j in range(11):
        print(i, "x", j, "=", i*j)


print("--------------------")