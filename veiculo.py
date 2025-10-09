class Veiculo:
    fabricante = ""
    modelo = ""
    ano = 0
    
    def __init__(self, fab, mod, ano):
        self.fabricante = fab
        self.modelo = mod
        self.ano = ano
    
    def info(self):
        print(self.fabricante, self.modelo, self.ano)

## os objetos estão no arquivo frota.py ##