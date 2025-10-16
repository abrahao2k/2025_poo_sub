from bicicleta import Bicicleta

bike1 = Bicicleta()

bike1.setMarca("Caloi")
bike1.setModelo("Ceci")
bike1.setCor("Branca")
bike1.setTamanho(24)

print(f"Você gosta as bicicletas {bike1.getMarca()}?")
print(f"Eu tenho uma {bike1.getModelo()} {bike1.getCor()}.")

