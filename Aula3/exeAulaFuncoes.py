nomes = ["da", "fa", "oi", "da"]
# index    0     1     2    3


def insert(nomesi: list, nome: str):
    nomesi.append(nome)
    return nomesi


def listar(nomesl: list):
    for nome in nomesl:
        print("nome : ", nome)


def delete(nomesd: list, posicao: int):
    nomesd.pop(posicao)
    return delete


def procurar(listaNomes: list, nomeAProcurar: str):
    indices = []
    for i in range(len(listaNomes)):
        if listaNomes[i] == nomeAProcurar:
            indices.append(i)
    return indices


while True:
    print("")
    print("1 - inserir nome")
    print("2 - listar nomes")
    print("3 - delete nome")
    print("4 - procurar nome")
    print("5 - sair")
    opt = input("Escolha Opção: ")
    match opt:
        case "1":
            insNome = input("insert um nome: ")
            insert(nomes, insNome)
            print("\nNome inserido com sucesso!")
        case "2":
            listar(nomes)
        case "3":
            nomeAProcurar = input("insert nome que quer apagar: ")
            posicoes = procurar(nomes, nomeAProcurar)
            if len(posicoes) > 0:
                print(f"\nForam encontrados {len(posicoes)} nomes:")
                for i in posicoes:
                    print("Nome: ", nomes[i], " Posição: ", i)
                nomeApagar = int(
                    input("\nInsira a posição para apagar o nome da lista: ")
                )
                delete(nomes, nomeApagar)
            else:
                print("\nNenhum nome encontrado.")
        case "4":
            nomeAProcurar = input("insert nome de procura: ")
            posicoes = procurar(nomes, nomeAProcurar)
            if len(posicoes) > 0:
                print(f"\nForam encontrados {len(posicoes)} nomes:")
                for i in posicoes:
                    print("Nome: ", nomes[i], " Posição: ", i)
            else:
                print("\nNenhum nome encontrado.")
        case "5":
            print("\nfim do programa")
        case _:
            print("\nnao escolheu a opçao certa")
