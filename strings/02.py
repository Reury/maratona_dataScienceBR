nome = input("Digite seu nome\n")
invertido = ""
tamanho = len(nome)
for x in reversed(nome):
    invertido += x
print(invertido.upper())
