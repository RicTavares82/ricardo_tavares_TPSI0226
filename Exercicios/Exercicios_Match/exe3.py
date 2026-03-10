# Exercício 3
# 3. Tipo de pedido
# Recebe um dicionário com as chaves "tipo" e "valor".
# Exibe:
# •	“Compra de X€” se tipo for “compra”
# •	“Venda de X€” se tipo for “venda”
# •	“Pedido desconhecido” caso contrário
# Exemplo:
# Entrada → {"tipo": "venda", "valor": 250}
# Saída → Venda de 250€


# pedido = {"tipo": "venda", "valor": 250} #Dicionário com os valores já declarados

tipo = input("Insira o tipo (compra/venda): ")
valor = int(input("Insira o valor: "))
pedido = {"tipo": tipo, "valor": valor}

if pedido["tipo"] == "compra":
    print(f"Compra de {pedido['valor']}€")
elif pedido["tipo"] == "venda":
    print(f"Venda de {pedido['valor']}€")
else:
    print("Pedido desconhecido")

print()
# -------------
# outra forma de mostrar o resultado

# tipo = input("Insira o tipo (compra/venda): ")
# valor = int(input("Insira o valor: "))
# pedido = {"tipo": tipo, "valor": valor}

match pedido:
    case {"tipo": "compra", "valor": valor}:
        print(f"Compra de {pedido['valor']}€")
    case {"tipo": "venda", "valor": valor}:
        print(f"Venda de {pedido['valor']}€")
    case _:
        print("Pedido desconhecido")
