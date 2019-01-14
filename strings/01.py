print("Compara 2 strings\n")
string1 = input("Digite uma frase :\n")
string2 = input("Digite outra frase:\n")

# tam_string1 = len(string1)
print("String 1: ", string1)
print("String 2: ", string2)
print("Tamanho de \"", string1, "\" :", len(string1)," caracteres")
print("Tamanho de \"", string2, "\" :", len(string2)," caracteres")
if(len(string1) != len(string2)):
    print("As duas strings são de tamanhos diferentes.")
else:
    print("Elas tem o mesmo tamanho")
if(string2 == string1):
    print("Voce digitou a mesma coisa")
else:
    print("As duas strings possuem conteúdo diferente.")
