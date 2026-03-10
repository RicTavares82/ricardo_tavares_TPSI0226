# Exercicio 7

# Pedir os valores ao utilizador
categoria = input("Digite a categoria (eletrônico/alimento): ")
if categoria != "alimento":
    preco = float(input("Digite o preço: "))
else:
    preco = 0

# Criar o dicionário com os valores digitados
luxo = {"Categoria": categoria, "Preço": preco}

# Lógica de verificação
# if luxo["Categoria"] == "eletronico" or "eletrônico" and luxo["Preço"] > 1000:
#     print("Produto de luxo")
# elif luxo["Categoria"] == "eletronico" or "eletrônico" and luxo["Preço"] <= 1000:
#     print("Produto comum")
# elif luxo["Categoria"] == "alimento":
#     print("Produto alimentar")
# else:
#     print("Categoria desconhecida")


match categoria:
    case {"Categoria": "eletronico", "Preço": preço}:
        print("Produto de luxo")
    case {"tipo": "venda", "valor": valor}:
        print("Produto comum")
    case _ if ["Categoria"] == "alimento":
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")
