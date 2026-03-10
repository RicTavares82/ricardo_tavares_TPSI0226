# Exercicio 7

# Pedir os valores
categoria = input("Digite a categoria (eletronico/alimento): ").lower()
if categoria != "alimento":
    preco = float(input("Digite o preço: "))
else:
    preco = 0

# Criar o dicionário com os valores digitados
luxo = {"Categoria": categoria, "Preço": preco}

# a lógica de verificação
# if luxo["Categoria"] == "eletronico" and luxo["Preço"] > 1000:
#     print("Produto de luxo")
# elif luxo["Categoria"] == "eletronico" and luxo["Preço"] <= 1000:
#     print("Produto comum")
# elif luxo["Categoria"] == "alimento":
#     print("Produto alimentar")
# else:
#     print("Categoria desconhecida")

# ----------------
# outra forma de apresentar a solução
match luxo:
    # Caso seja eletrónico E o preço seja maior que 1000
    case {"Categoria": "eletronico", "Preço": p} if p > 1000:
        print("Produto de luxo")

    # Caso seja eletrónico E o preço seja 1000 ou menos
    case {"Categoria": "eletronico", "Preço": p}:
        print("Produto comum")

    # Caso a categoria seja alimento (não importa o preço)
    case {"Categoria": "alimento"}:
        print("Produto alimentar")

    case _:
        print("Categoria desconhecida")
