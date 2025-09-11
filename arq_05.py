# modo append (acrescentar)
arq = open("juntada.txt", "a")

digitacao = input("Digite algo: ")

arq.write(digitacao + "\n")
# adicione o pulo de linha

arq.close()

print("Tá salvo!")