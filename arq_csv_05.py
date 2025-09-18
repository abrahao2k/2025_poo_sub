import csv

arq = open("produtos.csv","r",encoding="utf-8")

leitor = csv.reader(arq, delimiter=";")

dados = list(leitor) # converte o arquivo para lista/sublistas

arq.close()

print(dados)