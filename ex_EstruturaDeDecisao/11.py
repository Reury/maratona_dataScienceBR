salario = 0
aumento = 0
while(salario<1):
    salario = float(input("Digite o valor do salario\n"))
    novo_salario = 0
    if(salario<1):
        print("Valor informado não e compativel\ntente denovo\n")

if(salario <= 280):
    novo_salario = salario * 1.2
    aumento = novo_salario - salario
    print("O valor do salario antes do reajuste era ", salario)
    print("O percentual de aumento foi 20%")
    print("O valor do aumento foi de ", aumento)
    print("O novo valor e ", novo_salario)
elif(salario > 280 and salario<= 700):
    novo_salario = salario * 1.15
    aumento = novo_salario - salario
    print("O valor do salario antes do reajuste era ", salario)
    print("O percentual de aumento foi 15%")
    print("O valor do aumento foi de ", aumento)
    print("O novo valor e ", novo_salario)
elif(salario > 700 and salario<=1500):
    novo_salario = salario * 1.1
    aumento = novo_salario - salario
    print("O valor do salario antes do reajuste era ", salario)
    print("O percentual de aumento foi 10%")
    print("O valor do aumento foi de ", aumento)
    print("O novo valor e ", novo_salario)
elif(salario> 1500):
    novo_salario = salario * 1.05
    aumento = novo_salario - salario
    print("O valor do salario antes do reajuste era ", salario)
    print("O percentual de aumento foi 5%")
    print("O valor do aumento foi de ", aumento)
    print("O novo valor e ", novo_salario)
