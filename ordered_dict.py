'''
Modulo Collections: Ordered Dict

-> para o Ordered Dict a ordem do dicionario deve  ser a mesma se houve uma comparação (==)
'''

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}->valor={valor}')

from collections import OrderedDict

dic = OrderedDict({'a': 4, 'b': 6, 'r': 3, 'd': 2, 's': 7})     # garante a ordem em que foram inseridos os elementos.
print(dic)