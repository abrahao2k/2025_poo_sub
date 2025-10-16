#------------------------
# Bicicleta
#------------------------
# - marca: str
# - modelo: str
# - cor: str
# - tamanho: int
#------------------------
# + getMarca(): str
# + setMarca(str): void
# + getModelo(): str
# + setModelo(str): void
# + getCor(): str
# + setCor(str): void
# + getTamanho(): int
# + setTamanho(int): void
#------------------------

class Bicicleta:
    __marca   = ""
    __modelo  = ""
    __cor     = ""
    __tamanho = 0
    
    def getMarca(self):
        return self.__marca
    
    def setMarca(self, marca):
        self.__marca = marca
    
    def getModelo(self):
        return self.__modelo
    
    def setModelo(self, modelo):
        self.__modelo = modelo
    
    def getCor(self):
        return self.__cor
    
    def setCor(self, cor):
        self.__cor = cor
    
    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, tamanho):
        self.__tamanho = tamanho
    