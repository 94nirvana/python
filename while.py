num = 0
while num < 11:
    print(num)
    num += 1

print("-------")

resposta = ""

while resposta != "sim":
    resposta = input("Ja acabou jessica? ")


print("-------")


num = 0
while num <= 10:
    print(num)
    num += 1
    if num == 6:
        break

print("-------")

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break
    else:
        continue
