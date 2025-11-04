class Computador:
    __marca = ""         # encapsulamento / privado
    processador = ""    
    ram = 0
    hd = 0
    '''
    def __init__(self, m, p, r, h):
        self.__marca = m
        self.processador = p
        self.ram = r
        self.hd = h
    '''
    def getMarca(self):
        return self.__marca
    
    def setMarca(self, m):
        self.__marca = m
    
    def info(self):
        print(self.__marca)
        print(self.processador)
        print(self.ram)
        print(self.hd)

#########################################
class Notebook(Computador):
    bateria = 0
    tela = 0
    
    def info(self):          # sobrescrita (código diferente)
        super().info()
        print(self.bateria)
        print(self.tela)

#########################################

note1 = Notebook()
note1.setMarca("Samsung")
note1.bateria = 5000
note1.tela = 14.5

note1.info()



'''
comp4 = Computador("Dell", "I5", 8, 256)

comp4.setMarca("Lenovo")
print("Marca:", comp4.getMarca() )
'''

#comp4.info()

# print("Marca:", comp4.__marca) # privado, dá erro pois não vê
        
'''
comp1 = Computador()    # construtor (cria o objeto)
comp2 = Computador()
comp3 = Computador()

comp1.marca = "Dell"
comp1.processador = "I7"
comp1.ram = 16
comp1.hd = 480

comp1.info()
'''