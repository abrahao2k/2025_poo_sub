import csv
import os      # necessário para verificar se o arquivo existe

existe = os.path.exists("prod.csv")

arq = open("prod.csv","a",newline="")
grav = csv.writer(arq, delimiter=";")

if not existe :
    print("Criando novo arquivo.")
    grav.writerow(["Produto","Preço","Estoque"])
else:
    print("Atualizando arquivo existente.")

while True:
    nome = input("Nome do produto: ")
    preço = input("Preço do produto: ")
    qtd  = input("Quantidade estoque: ")
    grav.writerow([nome,preço,qtd])
    print("Gravado com sucesso.")
    
    op = input("Cadastrar outro? (s/n) ")
    if op == "n" : break

arq.close()