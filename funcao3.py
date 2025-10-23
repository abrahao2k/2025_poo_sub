def somar():
    v1 = int(input("Primeiro valor: "))
    v2 = int(input("Segundo valor: "))
    print(f"A soma é: {v1+v2}")
######################################################
def multiplicar():
    n1 = int(input("Valor 1: "))
    n2 = int(input("Valor 2: "))
    print(f"O produto é: {n1*n2}")
######################################################
def subtrair():
    x1 = int(input("Primeiro: "))
    x2 = int(input("Segundo: "))
    print(f"A diferença é: {x1-x2}")
######################################################
def dividir():
    k1 = int(input("V1: "))
    k2 = int(input("V2: "))
    print(f"O quociente é: {k1/k2}")
######################################################
while True:
    print("== CALCULADORA ==")
    print("1-Somar\n2-Multiplicar\n3-Subtrair\n4-Dividir")
    op= input("Qual operação? ")
    if   op == "1" : somar()
    elif op == "2" : multiplicar()
    elif op == "3" : subtrair()
    elif op == "4" : dividir()
             