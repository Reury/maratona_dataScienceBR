n1 = int(input("digite um numero:\n"))
n2 = int(input("digite um numero:\n"))
n3 = int(input("digite um numero:\n"))

if(n1>n2 and n1>n3 and n2>n3):
    print(n1)
    print(n2)
    print(n3)
elif(n2>n1 and n2>n3 and n1>n3):
    print(n2)
    print(n1)
    print(n3)
elif(n2>n1 and n2>n3 and n1<n3):
    print(n2)
    print(n3)
    print(n1)
elif(n3>n1 and n3>n2 and n1>n2):
    print(n3)
    print(n1)
    print(n2)
else:
    print(n3)
    print(n2)
    print(n1)
