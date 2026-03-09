# Exercício 6

# Pedir os valores ao utilizador
status = input("Digite o status (ok/erro): ")
tempo = int(input("Digite o tempo de resposta (ms): "))

# Criar o dicionário com os valores digitados
servidor = {"status": status, "tempo_resposta": tempo}

# Lógica de verificação
if servidor["status"] == "ok" and servidor["tempo_resposta"] > 200:
    print("Servidor lento")
elif servidor["status"] == "ok":
    print("Servidor ativo")
elif servidor["status"] == "erro":
    print("Servidor indisponível")
else:
    print("Estado desconhecido")
