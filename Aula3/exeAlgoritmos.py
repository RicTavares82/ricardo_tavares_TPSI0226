nomes = ["da", "fa", "oi", "da"]
# index    0     1     2    3


def insert(nomesi: list):
    nomesi.append(input("insert um nome: "))


def listar(nomesl: list):
    for nome in nomesl:
        print("nome : ", nome)


def delete(nomesd: list):
    nomesd.pop(int(input(" insert posiçao: ")))


# def procurar(nomesp: list):
#     nome = input("insert nome de procura: ")
#     for i in range(len(nomesp)):
#         if nomesp[i] == nome:
#             print("nome: ", nomesp[i], " na posiçao ", i)


def procurar(nomesp: list):
    nome_procurado = input("Insira o nome para procurar: ")
    indices_encontrados = []

    for i in range(len(nomesp)):
        if nomesp[i] == nome_procurado:
            indices_encontrados.append(i)

    return indices_encontrados


while True:
    print("1 - inserir nome")
    print("2 - listar nomes")
    print("3 - delete nome")
    print("4 - procurar nome")
    print("6 - sair")
    opt = input("Escolha Opção: ")
    match opt:
        case "1":
            insert(nomes)
        case "2":
            listar(nomes)
        case "3":
            # delete(nomes)
            pass
        case "4":
            # procurar(nomes)
            posicoes = procurar(nomes)
            if len(posicoes) > 0:
                print(f"\nForam encontrados {len(posicoes)} clientes com esse nome:")
                for idx in posicoes:
                    # Aqui podes mostrar todos os dados das tuas listas paralelas
                    print(" Nome: ", nomes)
            else:
                print("Nenhum cliente encontrado com esse nome.")
            # print aqui os valores e posiçoes
        case "5":
            break
        case "6":
            print("\nfim do programa")
            break
        case _:
            print("\nnao escolheu a opçao certa")
