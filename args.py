'''
Entendendo *args

- É um parametro de entrada de uma função, e voce pode chamar de qualquer coisa, desde que começe com asterisco.

exemplo:
*param

Mas por convencao usa-se *args
Coloca os valores extras informados como entrada em uma tupla. Entao desde ja lembre-se que são imutaveis.

'''


def soma(*args):
    return sum(args)


print(soma(2,3,4))
print(soma(2,2))
print(soma(3,4,5,6,7))
print(soma())


def verifica_info(*args):
    if "Geek" in args and "University" in args:
        return "Bem vindo Geek"
    return "Não tenho certeza quem voce é..."


print(verifica_info())
print(verifica_info(1, True, "University", "Geek"))
print(verifica_info(1, "University", 3.145))


numeros = [1, 2, 3, 4, 5]

print(soma(*numeros))