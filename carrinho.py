carrinho = []
resposta = ''
while resposta != 'nao':
    produto = {'nome': input("Digite o nome do produto: "),
               'quantidade': int(input("Digite a quantidade do produto: ")),
               'preco': float(input("Digite o preco do produto: "))
               }
    carrinho.append(produto)
    resposta = input("Continuar comprando? ")
print(carrinho)

