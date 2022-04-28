'''
**kwargs
-> exige chave e valor, e gera um dicionario.
-> Não são obrigatorios

ORDEM DOS PARAMETROS:
1º - Parametros obrigatorios
2º - *args
3º - Parametros default
4º - **kwargs
'''


def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')


cores(Alessandro='amarelo', Alex='verde', Venancio='azul')
print("-------------------------------------------------")
cores()
print("-------------------------------------------------")
cores(geek='vemerlho')
print("-------------------------------------------------")


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return "Voce recebeu um cumprimento Pythonico"
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    else:
        return "Nao sei quem vc é..."


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))

print("-------------------------------------------------")


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print("solteiro")
    else:
        print("casado")
    print(kwargs)


minha_funcao(33, 'Roberto', solteiro=True, cor='verde', estilo='grunge')
minha_funcao(34, 'Felipe', eu="não", voce="vai")
minha_funcao(19, 'Carla', 9, 3, 4, java=False, python=True)
print("-------------------------------------------------")


def mostra(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra(1, 2, 4, sobrenome='University', cargo='Instrutor'))
print("-------------------------------------------------")


# Desempacotamento:

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))
print("-------------------------------------------------")


def soma_multiplos(a, b, c):
    print(a+b+c)


lista = [1, 2, 4]
soma_multiplos(*lista)
print("-------------------------------------------------")
lista2 = {'a': 1, 'b': 2, 'c': 3}
soma_multiplos(**lista2)
print("-------------------------------------------------")
