import csv
arq = open("produtos.csv","r")
leitor = csv.reader(arq, delimiter=";")
dados = list(leitor) # converte o arquivo para lista/sublistas
arq.close()
print(dados)

dados.pop(1) # elimina um cadastro da lista
print(dados)

arq = open("produtos.csv","w",newline="")
grav = csv.writer(arq,delimiter=";")
grav.writerows(dados) # grava a lista toda de uma vez
arq.close()
print("Atualizado com sucesso.")