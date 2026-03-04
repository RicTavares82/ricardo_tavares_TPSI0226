# Exercício 1

# dia = input("Escreva o dia da semana: ")

# if dia == "domingo" or dia == "sábado":
#     print("Hoje é fim-de-semana")
# else:
#     print("Hoje é dia útil")


# ------------------------

# Exercício 2
# nota = int(input("Digite a nota do teste (0-100): "))

# if nota < 50:
#     print("Insuficiente")
# elif nota >= 50 and nota < 70:
#     print("Suficiente")
# elif nota >= 70 and nota < 90:
#     print("Bom")
# else:
#     print("Excelente")


# ------------------------
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


# pedido = {"tipo": "venda", "valor": 250}
# if pedido["tipo"] == "compra":
#     print(f"Compra de {pedido['valor']}€")
# elif pedido["tipo"] == "venda":
#     print(f"Venda de {pedido['valor']}€")
# else:
#     print("Pedido desconhecido")


# -------------------------
# Exercício 4

# float
med = 2.3
print(type(med))
print(med)

# string
nom = "João"
print(type(nom))
print(nom)

# listas []
lista = [1, 5, 3, 4, 9]
print(type(lista))
print(lista)

# --------------------------

# Exercício 5

mensagem = input("Escreva a sua mensagem: ").lower()  # .lower() para ignorar maiúsculas

# 1. Saudação (Comparação exata)
if mensagem == "olá" or mensagem == "bom dia":
    print("Saudação")

# 2. Pergunta (Verificar o último carater da mensagem)
elif mensagem.endswith("?"):
    print("Pergunta")

# 3. Despedida (Pesquisa de palavra dentro do texto)
elif "tchau" in mensagem or "adeus" in mensagem:
    print("Despedida")

# 4. Caso contrário
else:
    print("Mensagem genérica")


# -------------------------

# Exercício 6

# 1. Pedir os valores ao utilizador
st = input("Digite o status (ok/erro): ")
tempo = int(input("Digite o tempo de resposta (ms): "))

# 2. Criar o dicionário com esses valores
servidor = {"status": st, "tempo_resposta": tempo}
# Lógica de verificação
if servidor["status"] == "ok" and servidor["tempo_resposta"] > 200:
    print("Servidor lento")
elif servidor["status"] == "ok":
    print("Servidor ativo")
elif servidor["status"] == "erro":
    print("Servidor indisponível")
else:
    print("Estado desconhecido")
