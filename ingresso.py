class Ingresso:
    valor = 0
    def info(self):
        print("Valor: R$", self.valor)

#################################################
class IngressoVIP(Ingresso):
    adicional = 0
    def info(self):
        print("Valor VIP: R$", self.valor + self.adicional)

#################################################
ing = Ingresso() # Construtor
ing.valor = 35
ing.info()

vip = IngressoVIP()
vip.valor = 35
vip.adicional = 25
vip.info()