# acessar em outra pasta, use \\ no caminho
arquivo = open("c:\\dados\\info.txt","r")
texto = arquivo.read()
arquivo.close()

print(texto)

# se os acentos ficarem estranhos,
# mude a codificação do arquivo (ANSI/UTF-8)

arquivo = open("c:\\dados\\legal.txt","r", encoding="utf-8")
texto = arquivo.read()
arquivo.close()

print(texto)