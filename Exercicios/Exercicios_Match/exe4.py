# Exercício 4

valor = input("Insere algo para analisar: ")

match valor:
    case bool():
        print(type(valor))
        print(valor)
    case int():
        print(type(valor))
        print(valor)
    case float():
        print(type(valor))
        print(valor)
    case str():
        print(type(valor))
        print(valor)
    case list():
        print(type(valor))
        print(valor)
    case _:
        print("Tipo desconhecido")


# print()
# # float
# med = 2.3
# print(type(med))
# print(med)

# # string
# nom = "João"
# print(type(nom))
# print(nom)

# # listas []
# lista = [1, 5, 3, 4, 9]
# print(type(lista))
# print(lista)
