'''5. Crie um programa que solicita a digitação de nomes
de produtos. O usuário pode digitar quantos produtos desejar.
Armazene cada informação em uma lista. Por fim, classifique em 
ordem alfabética e grave a lista em um arquivo
chamado produtos.txt'''

produtos = []
while True:
    prod = input("Digite o produto: ")
    produtos.append(prod + "\n")
    op = input("Continuar? (s/n) ")
    if op == 'n' : break

produtos.sort()

arq = open("produtos.txt", "w")
arq.writelines(produtos)
arq.close()
print("Gravado com sucesso.")

