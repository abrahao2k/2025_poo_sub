'''1. Escreva o código de um programa que solicita a digitação
de dois valores e exibe a divisão do primeiro pelo segundo.
Use o tratamento de erros para evitar divisão por zero e 
valores não numéricos.
'''

try:
    n1 = int(input("Primeiro número: "))
    n2 = int(input("Segundo número: "))
    print("Divisão:", n1/n2)

except ZeroDivisionError:
    print("Divisão por zero. Escolha outro denominador.")

except ValueError:
    print("Não é um número válido. Tente novamente.")

