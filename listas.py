'''
Listas:
Listas em python funcionam como vetores ou matrizes(arrays), com a diferença de serem dinamicas e também podermos colocar QUALQUER tipo de dado.

- Dinâmico: Não possui tamanho fixo, podem ser adicionado e removidos elementos.
- Qualquer: Admite qualquer tipo de dado;

As listas em python são representadas por colchetes [].
'''

lista = [16,25,34,42,56,67,78,89,90,4]
for i in lista:
    print(i)

print(type(lista))

print('---------')

lista1 = [1,2,3,4,5,6,7,8,9,10,11]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = ['Geek University']
for i in lista2:
    print(i)

print('---------')

for i in lista4:
    print(i)

print('---------')

for i in lista5:
    print(i)

print('---------')

if 5 in lista4:
    print("Numero encontrado.")
else:
    print("Não encontrei o numero.")

print('---------')

if 'e' in lista2:
    print(lista2.count('e'))

print('---------')
# Ordenar uma lista
lista.sort()
print(lista)

print('---------')

'''
para adicionar elementos em listas utilizamos a função append. Adicionamos um elemento por vez, porem é possivel adicionar uma lista com varios elementos ex.:[1,2,3,4,[5,6,7,8]].
'''

a = [1,2,3]
a.append(4)
a.append(5)
print(a)

print('---------')
'''
Para remover e retornar(é possivel salvar em uma variavel) o ultimo elemento de uma lista utilizamos a função .pop():
'''
a.pop()
a.pop(2) # -> indicando o indice de remoção
print(a)

print('---------')
'''
Modificando um valor em uma lista:
'''
a[0] = 9
print(a)

print('---------')
'''
Adiciona varios elementos a lista .extend(lista ou valor):
'''
a.extend([11,12,13,14])
print(a)

print('---------')

'''
Podemos inserir um novo elemento na lista informando a posição do indice dele .insert(posicao, valor):
'''

a.insert(0, "Novo Valor")
print(a)


print('---------')
'''
Podemos juntar duas listas
'''
b=[9,8,7,6,5,4]
c = a + b   # poderia usar a.extend(b)
print(c)

print('---------')

'''
imprimir lista na ordem inversa .reverse():
'''
a.reverse()
print(a)

print('---------')

print(c[::-1]) # reverte a lista tambem.

print('---------')

'''
copiar uma lista .copy():
'''

g = c.copy()
print(g)

print('---------')
'''
Tamanho de uma lista (len):
'''
print(len(g))

print('---------')

'''
Podemos repetir elementos em uma lista:
'''

nova = [1,2,3]
nova *= 3
print(nova)

print('---------')

'''
Convertendo String em Lista:
'''

curso = "Programação em Python"
curso = curso.split() # separa entre os espaços entre os elementos, pode ser passado o tipo de separador entre "" dentro do split(), ex.: .split(",")
print(curso)

print('---------')
'''
Convertendo lista em String
'''
nova_lista = ['Programacao', 'em', 'Python']
nova_lista = " ".join(nova_lista)
print(nova_lista)

print('---------')
'''
Podemos criar lista com qualquer tipo de dados...
'''
new = [12, 3.45, True, "Geek", 455645640]
print(new)

print('---------')

'''
Uso do while com lista:
'''

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

print('---------')

for produto in carrinho:
    print(produto)

print('---------')

colorido = ['verde', 'amarelo', 'azul', 'branco']

for indice, cor in enumerate(colorido):
    print(indice, cor)

print('---------')

colorido = list(enumerate(colorido))
print(colorido)

print('---------')

'''
Metodos uteis:
- achar indice de um elemento -> print(lista.index(valor))
- caso haja mais de um elemento com o mesmo valor na lista sera retornado o indice do primeiro encontrado.
- podemos fazer busca dentro de um range de elementos, ou seja, em qual indice começar -> print(lista.index(valor, indice a partir da contagem))
- podemos fazer busca dentro de um range inicio/fim -> print(lista.index(valor, inicio, fim)
'''

'''
Slicing
'''

# lista[inicio, fim, passo]
# range[inicio, fim, passo]

listaa = [1,2,3,4,5,6]
print(listaa[1:]) # do indice 1 ate o final
print(listaa[1:3]) # do indice 1 ate o 3
print(listaa[0:5:1]) # do indice 0 ate o 5 de um em um, lembrando que o valor final (-1)
print(listaa[1::2]) # começa em 1, vai ate o final, de 2 em 2.

print('---------')

'''
Valores Numericos:
Soma -> print(sum(listaa))
Valor Máximo -> print(max(listaa))
Valor Minimo -> print(min(listaa))
Tamanho -> print(len(listaa))
'''


