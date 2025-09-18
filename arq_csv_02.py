import csv
arq = open("produtos.csv","w",newline="")
grav = csv.writer(arq, delimiter=";")
grav.writerow(["Produto","Preço","Estoque"])

while True:
    nome = input("Nome do produto: ")
    preço = input("Preço do produto: ")
    qtd  = input("Quantidade estoque: ")
    grav.writerow([nome,preço,qtd])
    print("Gravado com sucesso.")
    
    op = input("Cadastrar outro? (s/n) ")
    if op == "n" : break

arq.close()