######## PREENCHER A LISTA #########
nomes = []
while True: 
    nom = input("Digite um nome: ")
    nomes.append(nom + "\n")          # pular linha
    op = input("Continuar? (s/n) ")
    if op == 'n' : break

##### GRAVAR A LISTA NO DISCO #####
nomes.sort() # ordem alfabética

arq = open("nomes_lista.txt", "w")
arq.writelines(nomes)  # grava todos os itens da lista
arq.close()
print("Gravação da lista concluída.")