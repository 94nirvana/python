'''
Funcoes com parametro padrao: (default parameters)
- funcoes onde a passagem de parametro seja opcional
'''


def exponencial(num, expoente=2):
    return num ** expoente


print(exponencial(9, 3))
print(exponencial(3))


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))


def diz_oi():
    prof = "Geek"
    return f'Ola {prof}'


print(diz_oi())


def incrementa():
    total = 0
    total += 1
    return total


print(incrementa())