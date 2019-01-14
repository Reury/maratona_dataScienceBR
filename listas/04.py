frase = input("Digite uma letra: \n")
frase = frase[:11]
whitespace = 0
volgal = ""
consoante = ""
for i in frase:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        volgal += i
    elif (i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        volgal += i
    elif(i == " "):
        whitespace += 1
    else:
        consoante += i


print(consoante)
print(len(consoante))

