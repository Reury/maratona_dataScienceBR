data_nasc = input("Digite a data de nascimento:\n")
tamanho = len(data_nasc)
dia = data_nasc[:2]
mes = data_nasc[3:5]
ano = data_nasc[tamanho-4:]

mes_extenso = "janeiro"

if(mes == "01"):
    mes_extenso = "janeiro"
elif(mes == "02"):
    mes_extenso = "fevereiro"
elif(mes == "03"):
    mes_extenso = "março"
elif(mes == "04"):
    mes_extenso = "Abril"
elif(mes == "05"):
    mes_extenso = "Maio"
elif(mes == "06"):
    mes_extenso = "junho"
elif(mes == "07"):
    mes_extenso = "julho"
elif(mes == "08"):
    mes_extenso = "Agosto"
elif(mes == "09"):
    mes_extenso = "Setembro"
elif(mes == "10"):
    mes_extenso = "Outubro"
elif(mes == "11"):
    mes_extenso = "novembro"
elif(mes == "12"):
    mes_extenso = "Dezenbro"


print("Voce nasceu em ", dia, " de ", mes_extenso, " de ", ano)


#
# print(mes_extenso)
# print(dia)
# print(mes)
# print(ano)
