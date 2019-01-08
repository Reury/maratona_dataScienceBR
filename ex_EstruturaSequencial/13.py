sexo = input("digite o sexo:\n")
altura = float(input("Digite sua altura em metros"))
if(sexo == 'M' or sexo == 'm'):
    t_peso = (72.9 * altura) - 58
else:
    t_peso = (62.1 * altura) - 44.7

print("Seu peso ideal e:\n", t_peso, " Kg\n")