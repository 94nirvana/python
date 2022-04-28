receita = {'jan': 1000, 'fev': 2500, 'mar': 3000}

# Iterar em dicionarios:
print(receita)

for chave in receita:
    print(chave)

print('-------------')

for chave in receita:
    print(receita[chave])

print('---------------')

for chave in receita:
    print(f'{chave}: {receita[chave]}')

print('---------------')

# >>> Valor MAX, MIN, e Tamanho <<< #
# SOMENTE PARA VALORES REAIS #

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))