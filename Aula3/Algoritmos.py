#
# ALGORITMOS

nomes = ["Maria", "João", "Pedro", "Ana", "Carla"]
# index       0      1        2       3        4


# funções sem return
def insert(nomesi: list):
    nomesi.append(input("insert um nome"))


def listar(nomesl: list):
    for nome in nomesl:  # para cada nome na lista de nomes faça  ---> FOREACH
        print("nome : ", nome)


def delete(nomesd: list):
    nomesd.pop(int(input(" insert posiçao ")))


def procurar(nomesp: list):
    nome = input("insert nome a procurar")
    for i in range(len(nomesp)):
        if nome == nomesp[i]:
            print("nome encontrado", nomesp[i])
            break


# procurar nome usando o operador in
if nome in nomesp:
    print("nome encontrado", nomesp[i])
else:
    print("nome não encontrado")


while True:
    print("1 - inserir nome")
    print("2 - listar nomes")
    print("3 - delete nome")
    print("4 - sair")
    opt = input("Escolha opção: ")
    match opt:
        case "1":
            insert(nomes)
            print(nomes)
        case "2":
            pass
        case "3":
            pass
        case "4":
            print("fim do programa")
        case _:
            print("não escolhei a opção certa")
