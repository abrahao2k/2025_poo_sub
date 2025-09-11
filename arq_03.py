# modo "r" (read) - leitura
arquivo = open("segundo.txt", "r")
texto = arquivo.read()
arquivo.close()

print(texto)
