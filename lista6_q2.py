'''2. Escreva um programa que solicite a digitação de
5 títulos de filme e grave as informações 
em um arquivo chamado filmes.txt. Use o tratamento de erros.'''

try:
    arq = open("filmes.txt","a")  # ou modo "w"

    for x in range(5):
        filme = input("Digite o título do filme: ")
        arq.write(filme + "\n")
        
    print("Gravado com sucesso.")

except:
    print("Erro gravando dados.")

finally:
    arq.close()