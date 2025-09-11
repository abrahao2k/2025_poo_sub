try:
    arq = open("juntada.txt", "r")
    arq.write("ok")
    arq.close()
    print(dados)
    
except FileNotFoundError:
    print("Arquivo não encontrado.")

except:
    print("Erro acessando arquivo.")