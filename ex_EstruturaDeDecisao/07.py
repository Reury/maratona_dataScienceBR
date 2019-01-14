i = 0
n1 = 0
n2 = 0
n3 = 0

while (n1 == n2 or n1 ==n3 or n2 == n3 ):
    n1 = int(input("Digite um numero\n"))
    n2 = int(input("Digite um numero\n"))
    n3 = int(input("Digite um numero\n"))
    if(n1 == n2 or n1 ==n3 or n2 == n3 ):
        print("favor não digitar numeros iguais\n")




if(n1> n2 and n1>n3):
    print(n1, " e o maior deles")
elif(n2>n1 and n2>n3):
    print(n2, " e o maior deles")
elif(n3>n1 and n3>n2):
    print(n3, " e o maior deles")

if(n1< n2 and n1<n3):
    print(n1, " e o menor deles")
elif(n2<n1 and n2<n3):
    print(n2, " e o menor deles")
elif(n3<n1 and n3<n2):
    print(n3, " e o menor deles")
