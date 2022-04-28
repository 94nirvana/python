'''
Reduce

A partir do Python3+ a funcao reduce() não é mais uma funcao integrada. Agora temos que importar o modulo functools.

A funcao reduce recebe dois parametros: a funcao e o interavel.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
-> res = f(a1, a2) # Aplica a funcao nos dois primeiros elementos da coleção e guarda o resultado.
-> res2 = f(res, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o resultado.
-> Isso se repete até o ultimo elemento.
Ou seja em cada passo ela aplica a funcao pasando como pimeiro argumento o resultado da apliação anterior.
No final, reduce() irá retornar o resultado final.

funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
'''

from functools import reduce

dados = [2, 3, 4, 5, 7, 8, 9, 6, 5, 4, 7, 8, 9, 4, 13, 29, 31, 45, 67, 65, 43, 21]

mult = lambda x, y: x * y

res = reduce(mult, dados)
print(res)

print('-------------------------------')

res = 1
for n in dados:
    res = res * n
print(res)
print('-------------------------------')

