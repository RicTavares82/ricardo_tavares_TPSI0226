# Exercício 6

# Pedir os valores ao utilizador
status = input("Digite o status ( ok / erro ): ")
tempo = int(input("Digite o tempo de resposta (ms): "))

# Criar o dicionário com os valores digitados
servidor = {"status": status, "tempo_resposta": tempo}

# # Lógica para verificação
# if servidor["status"] == "ok" and servidor["tempo_resposta"] > 200:
#     print("Servidor lento")
# elif servidor["status"] == "ok":
#     print("Servidor ativo")
# elif servidor["status"] == "erro":
#     print("Servidor indisponível")
# else:
#     print("Estado desconhecido")

# -------------------------
# outra forma de apresentar o mesmo resultado

match servidor:
    case {"status": "ok", "tempo_resposta": t} if t > 200:
        print("Servidor lento")
    case {"status": "ok"}:
        print("Servidor ativo")
    case {"status": "erro"}:
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")
