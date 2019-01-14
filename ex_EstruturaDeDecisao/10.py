turno = input("Em qual turno você estuda: \nFavor prencher com (m)Matutino (v) Vespertino (n)Noturno")
if(turno == 'm' or turno == "M"):
    print("Bom Dia!\n")
elif(turno == 'v' or turno == 'V'):
    print("Boa Tarde!\n")
elif(turno == 'n' or turno == 'N'):
    print("Boa Noite!")
else:
    print("Valor invalido!\n")
