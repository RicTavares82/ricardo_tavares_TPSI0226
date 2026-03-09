# Exercicio 9

# Pedir os valores ao utilizador
metodo = input("Digite o metodo (GET/POST): ")
conteudo = input("Digite o conteudo (" "/preenchido): ")

# Criar o dicionário com os valores digitados
requisicao = {"metodo": metodo, "conteudo": conteudo}

# Lógica de verificação
if requisicao["metodo"] == "POST" and requisicao["conteudo"] != " ":
    print("Requisição POST com dados válidos")
elif requisicao["metodo"] == "POST" and requisicao["conteudo"] == " ":
    print("Produto comum")
elif requisicao["metodo"] == "GET":
    print("Requisição GET recebida")
else:
    print("Método não suportado")
