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
# elif nota >=90 and nota < 101:
#     print("Excelente")
# else:
#     print("numero de nota errado")


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

# ????????
# pedido = {"tipo": "venda", "valor": 250}
# if pedido["tipo"] == "compra":
#     print(f"Compra de {pedido['valor']}€")
# elif pedido["tipo"] == "venda":
#     print(f"Venda de {pedido['valor']}€")
# else:
#     print("Pedido desconhecido")


# -------------------------
# Exercício 4

# ???????????
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

# --------------------------

# Exercício 5

# mensagem = input(
#     "Escreva a sua mensagem: "
# ).lower()  # .lower() para passar a maiúsculas

# # Saudação (Comparação exata)
# if mensagem == "olá" or mensagem == "bom dia":
#     print("Saudação")

# # Pergunta (Verificar o último carater da mensagem)
# elif mensagem.endswith("?"):
#     print("Pergunta")

# # Despedida (Pesquisa de palavra dentro do texto)
# elif "tchau" in mensagem or "adeus" in mensagem:
#     print("Despedida")

# # Caso contrário
# else:
#     print("Mensagem genérica")


# -------------------------

# Exercício 6

# # Pedir os valores ao utilizador
# status = input("Digite o status (ok/erro): ")
# tempo = int(input("Digite o tempo de resposta (ms): "))

# # Criar o dicionário com os valores digitados
# servidor = {"status": status, "tempo_resposta": tempo}

# # Lógica de verificação
# if servidor["status"] == "ok" and servidor["tempo_resposta"] > 200:
#     print("Servidor lento")
# elif servidor["status"] == "ok":
#     print("Servidor ativo")
# elif servidor["status"] == "erro":
#     print("Servidor indisponível")
# else:
#     print("Estado desconhecido")


# ----------------------------

# Exercicio 7

# # Pedir os valores ao utilizador
# categoria = input("Digite a categoria (eletrônico/alimento): ")
# if categoria != "alimento":
#     preco = float(input("Digite o preço: "))
# else:
#     preco = 0

# # Criar o dicionário com os valores digitados
# luxo = {"Categoria": categoria, "Preço": preco}

# # Lógica de verificação
# if luxo["Categoria"] == "eletrônico" and luxo["Preço"] > 1000:
#     print("Produto de luxo")
# elif luxo["Categoria"] == "eletrônico" and luxo["Preço"] <= 1000:
#     print("Produto comum")
# elif luxo["Categoria"] == "alimento":
#     print("Produto alimentar")
# else:
#     print("Categoria desconhecida")


# --------------------------------

# Exercicio 8

# num1 = int(input("Escreva um numero: "))
# num2 = int(input("Escreva outro numero: "))

# print("Escolha o tipo de operação de calculo.")
# print("1 - Somar")
# print("2 - Subtrair")
# print("3 - Multiplicar")
# print("4 - Dividir")
# opc = input("Selecione o numero: ")

# # soma=input("1 - Soma ")
# # sub=input("2 - ")

# match opc:
#     case "1":
#         print(f"{num1 + num2}")
#     case "2":
#         print(f"{num1 - num2}")
#     case "3":
#         print(f"{num1 * num2}")
#     case "4":
#         print(f"{num1 / num2}")


# ---------------------

# Exercicio 9

# # Pedir os valores ao utilizador
# metodo = input("Digite o metodo (GET/POST): ")
# conteudo = input("Digite o conteudo (" "/preenchido): ")

# # Criar o dicionário com os valores digitados
# requisicao = {"metodo": metodo, "conteudo": conteudo}

# # Lógica de verificação
# if requisicao["metodo"] == "POST" and requisicao["conteudo"] != " ":
#     print("Requisição POST com dados válidos")
# elif requisicao["metodo"] == "POST" and requisicao["conteudo"] == " ":
#     print("Produto comum")
# elif requisicao["metodo"] == "GET":
#     print("Requisição GET recebida")
# else:
#     print("Método não suportado")


# -------------------------

# Exercicio 10

continuar = "sim"
while continuar == "sim":
    j1 = "a"
    j2 = "a"
    print()
    while j1 != "pedra" and j1 != "papel" and j1 != "tesoura":
        # pequena validação da inserção
        print("Escolha a jogada => pedra, papel ou tesoura")
        j1 = input("Jogador 1: ")
    print()
    while j2 != "pedra" and j2 != "papel" and j2 != "tesoura":
        # pequena validação da inserção
        print("Escolha a jogada => pedra, papel ou tesoura")
        j2 = input("Jogador 2: ")

    # if j1 != "pedra" or j1 != "papel" or j1 != "tesoura":
    #     print("Jogada errada, repete: ")
    #     j1 = input("Jogador 1: ")
    # j2 = input("Jogador 2: ")
    # if j2 != "pedra" or j2 != "papel" or j2 != "tesoura":
    #     print("Jogada errada, repete: ")
    #     j2 = input("Jogador 2: ")

    print()
    # cria um match nas duas variaveis/valores (usa um tuplo)
    match (j1, j2):
        case _ if (
            j1
            == j2  # _ isto faz o case aceitar qualquer coisa. Neste caso, aceitar dentro do (j1, j2)
        ):
            print("Resultado: Empate!")

        # Casos em que o Jogador 1 ganha
        case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
            print("Resultado: Jogador 1 venceu!")

        # Casos em que o Jogador 2 ganha
        case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
            print("Resultado: Jogador 2 venceu!")

        case _:
            print("Erro: Jogada inválida! Usar apenas: ")
            print("pedra")
            print("papel")
            print("tesoura")
    print()
    continuar = input("Quer repetir o jogo? (sim/não): ")
