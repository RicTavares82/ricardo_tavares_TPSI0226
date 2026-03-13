# Dicionarios

# {} <---- dicionarios ---> tipo de ficheiro json
# chave - valor

carros = {"Marca": "BMW", "Modelo": "M3"}
# acesso tipo mapping

print()
#
print(carros)
print()
print(carros["Marca"])
print()
print(carros["Modelo"])

print()
# adicionar uma nova key (por exemplo Cor)
carros.update({"Cor": "Branco"})
print(carros)

print()
# actualizar algum valor de uma key (por exemplo Marca)
# quando é usada a mesma keys ele actulaiza o que lá metermos
carros.update({"Marca": "Fiat"})
print(carros)

print()
# apagar uma key
carros.pop("Marca")
print(carros)
