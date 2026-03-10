# Exercicio 10

repet = "sim"
while repet == "sim":
    j1 = "a"
    j2 = "a"
    print()
    while (
        j1 != "pedra" and j1 != "papel" and j1 != "tesoura"
    ):  # pequena validação da inserção
        print("Escolha a jogada => pedra, papel ou tesoura")
        j1 = input("Jogador 1: ")
    print()
    while (
        j2 != "pedra" and j2 != "papel" and j2 != "tesoura"
    ):  # pequena validação da inserção
        print("Escolha a jogada => pedra, papel ou tesoura")
        j2 = input("Jogador 2: ")

    print()
    # cria um match nas duas variaveis/valores (usa um tuplo)
    match (j1, j2):
        case _ if (
            j1 == j2
        ):  # _ isto faz o case aceitar qualquer coisa. Neste caso, aceitar dentro do (j1, j2)
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
    print("Quer repetir o jogo?")
    repet = input("(s = sim / n = não) ")
