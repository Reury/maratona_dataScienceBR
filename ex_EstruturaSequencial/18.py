tamanho = int(input("informe o tamanho do download\n"))
velocidade = int(input("informe a velocidade da conexao\n"))

eta = tamanho / velocidade
print("Vai demorar ", eta, " segundos")
