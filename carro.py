import random
### CLASSE CARRO ################################
class Carro:
    modelo = ""
    cor = ""
    posicao = 0
    
    def buzinar(self):
        print(self.modelo, self.cor)
        print("Biiiiiiiiiiiii")
    
    def andar(self):
        passos = random.randint(1,10)
        self.posicao += passos
        print(f"{self.modelo} {self.cor} andou {passos} metros. POS:{self.posicao}")
        

### OBJETOS #####################################
c1 = Carro()
c1.modelo = "Gol"
c1.cor = "Vermelho"

c2 = Carro()
c2.modelo = "Palio"
c2.cor = "Preto"

print("=== INÍCIO DA CORRIDA ===")

while c1.posicao < 100 and c2.posicao < 100 :
    c1.andar()
    c2.andar()
    print("---------------------------------------")

if c1.posicao > c2.posicao : print(c1.modelo, c1.cor, "VENCEU.")
elif c2.posicao > c1.posicao : print(c2.modelo, c2.cor, "VENCEU.")
else: print("EMPATE")
    