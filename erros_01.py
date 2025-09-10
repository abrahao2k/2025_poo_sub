try:
    numero = int(input("Digite um número: "))
    print("Você digitou", numero)

except (ValueError, TypeError):
    print("Erro de valor. Verifique a digitação.")

except NameError:
    print("Erro de nome. Comando ou variável desconhecidos.")

except:
    print("Erro misterioso.")

finally:
    print("Acaboooooouuuuu....")