# Exercicio 9

# Pedir os valores ao utilizador
metodo = input("Digite o metodo (GET/POST): ").lower()
conteudo = input("Digite o conteudo ((deixar vazio)/preenchido): ").lower()

# Criar o dicionário com os valores digitados
requisicao = {"metodo": metodo, "conteudo": conteudo}

# Lógica de verificação
if requisicao["metodo"] == "post" and requisicao["conteudo"] != "":
    print("Requisição POST com dados válidos")
elif requisicao["metodo"] == "post" and requisicao["conteudo"] == "":
    print("Requisição POST sem dados")
elif requisicao["metodo"] == "get":
    print("Requisição GET recebida")
else:
    print("Método não suportado")
