notas = []
media = 0
for i in range(4):
    notas.append(int(input("Digite a nota:\n")))
    print((i+1)," nota foi ", notas[i])
    media += notas[i]
media /= 4
print("A media foi :\n", media)
