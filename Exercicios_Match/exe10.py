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
