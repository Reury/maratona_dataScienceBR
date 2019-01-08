vlr_hora = (float(input("Qual o valor da sua hora :\n")))
hr_trabalhadas = (float(input("Quantas horas vc trabalhou: \n")))
vlr_salario = vlr_hora*hr_trabalhadas

ir = vlr_salario * 0.11
inss = vlr_salario * 0.08
sindicato = vlr_salario * 0.05
sal_liquido = vlr_salario - ir - inss - sindicato

print("Muito Bem Vamos ver quanto vc faturou:\n")
print("+ Salário Bruto : R$", vlr_salario, "\n")
print("- IR (11%) : R$", ir, "\n")
print("- INSS (8%) : R$", inss, "\n")
print("- Sindicato ( 5%) : R$", sindicato, "\n")
print("= Salário Liquido : R$", sal_liquido, "\n")
