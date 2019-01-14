vetor = []
pares = []
impares = []


for i in range(20):
    vetor.append(int(input("Digite um numero")))


for i in vetor:
    if(i % 2 == 0 ):
        pares.append(i)
    else:
        impares.append(i)

print("o vetor digitado foi :", vetor)
print("pares sao : ", pares)
print("impares sao :", impares)
