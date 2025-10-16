class Pessoa:
    __nome  = "Kátia"    # private
    __idade = 20         # private
    
    ## NOME ##################################
    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome
    
    ## IDADE #################################
    def getIdade(self):
        return self.__idade
    
    def setIdade(self, idade):
        if idade < 0 :          # validação do valor
            idade = 0
            
        self.__idade = idade

##############################################
p1 = Pessoa() # criar o objeto
#print(p1.__idade)
print( p1.getNome(), p1.getIdade() )
p1.setNome("Kátia Lima")
p1.setIdade(21)
print( p1.getNome(), p1.getIdade() )
