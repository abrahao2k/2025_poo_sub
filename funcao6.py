#FUNÇÕES COM RETORNO
def area_retangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura)/2

def area_circulo(raio):
    return 3.14 * raio * raio

##############################################

total = area_retangulo(4,3) + 10

print("Resultado =",  total)

