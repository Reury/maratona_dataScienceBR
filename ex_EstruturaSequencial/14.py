peso_peixes = float(input("Digite o peso total do pescado:\n"))
excesso = peso_peixes - 50
if(excesso<=0):
    print("Não houve multa pois o pescado não excedeu o limite de peso\n")
else:
    multa = excesso *4
    print("Houve um excesso de ", excesso, " Kg\n", "Portanto pagaras ",
          multa, " reais de multa\n", "referente ao excedente")
