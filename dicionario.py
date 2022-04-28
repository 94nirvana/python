'''
Dicionarios

OBS: Em algumas linguagens são conhecidos como mapas

São coleções do tipo chav/valor.

dic = {'a': 3, 'b': 4, 'c': 5}

- Dicionarios são representados por chaves {}
- Chave/Valor separados por :
- Tanto chave como valor podem ser de qualquer tipo de dado
- Podemos misturar tipos de dados

'''
# Forma comum
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Praraguai'}

print(paises)
print(type(paises))

print('---------------')
# Outra forma menos comum

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

print('---------------')

# Acessando elementos:
# - Acesso via chave, da mesma forma que em listas e tuplas.

print(paises['br'])
print(paises['py'])

print('---------------')
# Forma ideal de acessar os dados:

print(paises.get('br'))
print(paises.get('eua'))

print('---------------')

# Podemos definir um padrao caso nao encontre o objeto especifico:
pais = paises.get('ru', 'Nao encontrado')

print(f'Encontrei o {pais}')

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises) # -> Não busca por valor, somente pela chave.

print('---------------')

localidades = {
    (35.6895, 39.6917): 'Escritorio em Tokio',
    (40.7128, 740060): 'Escritorio em Nova York',
    (37.7749, 122.4194): 'Escritorio em São Paulo',
}
print(localidades)
print(type(localidades))

print('---------------')

novo_dado = {(934.4567, 24.7654): 'Escritorio em Madri'}
localidades.update(novo_dado)

print(localidades)

print('---------------')

# Conclusão, ao adicionarmos elementos ou atualizarmos dados em um dicionario é a mesma.
# Em dicionarios NAO podemos ter chaves repetidas.

### Remover dados de um dict ###

localidades.pop((37.7749, 122.4194))
print(localidades)
localidades.pop((35.6895, 39.6917)) # Retorna o valor removido, se necessario em uma variavel
print(localidades)

print('---------------')

# Outra forma

del localidades[(40.7128, 740060)] # Nao retorna valor em variavel
print(localidades)

print('---------------')

carrinho = []
produtos = {
    'nome': 'abacate',
    'quantidade': 3,
    'preco': 4.15,
}
carrinho.append(produtos)
print(carrinho)

print('---------------')
# >>> Zerar Dicionario <<< #
d = dict(a=1, b=2, c=3)
print(d)
d.clear()
print(d)

print('---------------')
# >>> Copiando Dicionario <<< #
d = dict(a=1, b=2, c=3)

novo = d.copy()
print(novo)
novo['d'] = 4
print(novo)

print('---------------')
# outro metodo bem estranho

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

print('---------------')

