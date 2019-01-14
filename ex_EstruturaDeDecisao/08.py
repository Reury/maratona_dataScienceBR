p1 = float(input("Digite o valor do primeiro produto"))
p2 = float(input("Digite o valor do segundo produto"))
p3 = float(input("digite o valor do terceiro produto"))

if(p1<p2 and p1<p3):
    print("compre o produto p1 que custa:\n", p1)
elif(p2<p1 and p2<p3):
    print("compre o produto p2 que custa:\n", p2)
else:
    print("compre o produto p3 que custa:\n", p3)

