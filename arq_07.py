arq = open("dados.txt", "r")

nome = arq.readline()     # readline() - lê uma linha por vez
email = arq.readline()
telefone = arq.readline()

arq.close()

print(f'''Oi, me chamo {nome.strip()}.
Esses são meus contatos: {email.strip()}, {telefone.strip()}.''')

# strip() - remove o pulo de linha do final da string
# rstrip('\n') - indica qual caractere remover