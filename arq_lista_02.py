### CARREGAR OS DADOS DE UM ARQUIVO PARA UMA LISTA ###

arq = open("nomes_lista.txt", "r")
nomes = arq.readlines() #cada linha vai pra uma posição da lista
arq.close()

print(nomes)

# remover o \n ao acessar um item individualmente

#print(f"Oi, {nomes[0].strip()}. Seja bem vindo.")