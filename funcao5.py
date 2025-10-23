lista = [1,2,3] # variavel global (funciona em qualquer parte)

def area_retangulo(base, altura): # variável local (só na função)
    print("Área do retângulo =", base*altura, "cm²")
    #print(lista)

def area_triangulo(base, altura):
    print("Área do triangulo =",(base*altura)/2, "cm²")
    
def area_circulo(raio):
    print("Área do círculo:", 3.14*raio*raio)

#################################
area_retangulo(12, 6)
print(base)
#area_triangulo(3, 5)
#area_circulo(4)