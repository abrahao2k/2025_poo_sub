class Copo:
    __capMaxima = 0
    __capAtual = 0
    __cor = ""
    __material = ""
    
    def getCapAtual(self):
        return self.__capAtual
    
    def setCor(self, cor):
        self.__cor = cor
    
    def setMaterial(self, mat):
        self.__material = mat
    
    def setCapMaxima(self, cap):
        self.__capMaxima = cap
    
    def info(self):
        print(f'''O copo {self.__cor} de {self.__material}
armazena até {self.__capMaxima}ml e no momento
tem {self.__capAtual}ml de líquido.''')
    
    def encher(self):
        self.__capAtual += 100
        if self.__capAtual > self.__capMaxima:
            print("O copo esborrou.")
            self.__capAtual = self.__capMaxima
        
    def esvaziar(self):
        self.__capAtual -= 100
        if self.__capAtual <= 0 :
            print("O copo está vazio.")
            self.__capAtual = 0
    
    