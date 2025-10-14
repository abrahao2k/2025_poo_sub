class Usuario:
    nome = "João"      # acesso público (public)
    __senha = "123"   # acesso privado (private)
    
    def info(self):
        print(self.nome, self.__senha)
    
#################################################

usu = Usuario()

print(usu.nome)
#print(usu.__senha)  # não enxerga, dá erro

usu.info()

