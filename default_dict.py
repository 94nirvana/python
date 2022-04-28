'''
Modulo Collections - Default Dict

Default Dict -> Ao criar um dicionario utilizando-o, nos informamos um valor defaullt,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave sera criada
e o valor default será atribuido.
'''

dic = {'curso': 'programacao em python essencial'}

print(dic)

print('--------------')

print(dic['curso'])

print('--------------')

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

print('--------------')

dicionario['curso'] = 'Programacao em Python: Essencial'

print(dicionario['outro'])

print('--------------')

print(dicionario)

print('--------------')