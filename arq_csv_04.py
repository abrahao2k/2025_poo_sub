# ler como texto

arq = open("produtos.csv","r",encoding="utf-8")
conteudo = arq.read()
arq.close()

print(conteudo)

