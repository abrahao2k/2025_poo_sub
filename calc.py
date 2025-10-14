class Calculadora:
    
    def somar(self, v1, v2):
        print("A soma é:", v1 + v2)
    
    def multiplicar(self, n1, n2):
        print("O produto é:", n1 * n2)
    
    def subtrair(self, p1, p2):
        pass


class Mesa:
    pass

m1 = Mesa()

#######################################
calc1 = Calculadora()

calc1.somar(5, 12)
calc1.multiplicar(5, 12)
calc1.subtrair(12,5)


