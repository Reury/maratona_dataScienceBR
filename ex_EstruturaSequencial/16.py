import math
area = int(input("Digite o tamanho da area a ser pintada: \n"))
lata = 54
qtd_latas = area / lata
qtd_latas = math.ceil(qtd_latas)
custo = qtd_latas * 80
custo = math.floor(custo)
if(area < lata):
    print("E necessario :\n", "1 lata\n","R$ ", custo, " reais a pagar")
else:
    print("E Necessario :\n", qtd_latas, " latas,\n",custo, " reais a pagar")