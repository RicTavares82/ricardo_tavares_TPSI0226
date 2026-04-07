# Teste Final: Elabore uma base de dados de clientes de uma fábrica de materiais. O programa deverá possibilitar inserção e listagem dos clientes bem como as compras por eles efetuadas( Númcli(Automático), NomCli, morada, tel, nif, compra, Divfin ). Divida final=compra – desconto, valor do desconto se compra for entre 100 e 200 é 5%, se for superior a 200 e inferior a 500 é 10% se superior a 500 é 15%. O programa deve validar todas as entradas e na listagem deve parar cliente a cliente e ser possível busca direta por número de cliente.


# ids = ["1", "2", "3", "4", "5"]
ids = [1, 2, 3, 4, 5]
nomes = ["da", "ra", "fa", "ta", "da"]
moradas = ["da", "ra", "fa", "ta", "da"]
telefones = ["10", "10", "10", "10", "10"]
nifs = ["10", "10", "10", "10", "10"]
compras = [10.5, 10.5, 10, 10, 10]
divfin = [10.5, 10.5, 10, 10, 10]

while True:
    print("")
    print("   ------MENU------")
    print("1 - Inserir novo cliente")
    print("2 - remover cliente")
    print("3 - pesquisar cliente")
    print("4 - editar cliente")
    print("5 - listar clientes")

    while True:
        num = input("\nEscolha uma opção: ")
        if num > "0" and num < "7":
            break
        else:
            print("\nEscreva um numero válido entre 1 e 6: ")

    match num:
        case "1":
            print("Inserir novo cliente")
            while True:
                ids.append(len(ids) + 1)
                nomes.append(input("Nome: "))
                moradas.append(input("Morada: "))
                while True:
                    novoTelefone = input("Telefone: ").strip()
                    if len(novoTelefone) == 9 and novoTelefone.isdigit():
                        telefones.append(novoTelefone)
                        break
                    else:
                        print("\nTelefone inválido! Deve conter exatamente 9 dígitos.")
                # telefones.append(input("Telefone: "))
                while True:
                    novoNif = input("NIF: ").strip()
                    if len(novoNif) == 9 and novoNif.isdigit():
                        nifs.append(novoNif)
                        break
                    else:
                        print("NIF inválido! Deve conter exatamente 9 dígitos.")
                # nifs.append(input("NIF: "))
                valorcompras = float(input("valor da compra: "))
                compras.append(valorcompras)

                if 100 <= valorcompras <= 200:
                    desconto = 5
                elif 200 < valorcompras < 500:
                    desconto = 10
                elif valorcompras >= 500:
                    desconto = 15
                else:
                    desconto = 0
                divfin.append(valorcompras - (valorcompras * (desconto / 100)))

                print("\nCliente inserido com sucesso!!!")
                perguntaSair = input("\nQuer inserir mais clientes? s/n: ")
                if perguntaSair == "n":
                    break
                print("")

        case "2":
            print("remover cliente")
            procurarNome = input("\nEscreva o nome ou ID a remover: ").strip()
            encontrou = False
            for i in range(len(ids)):
                if nomes[i] == procurarNome:
                    print(
                        f"\nPosição {i} | ID {ids[i]} | Nome: {nomes[i]} | Morada: {moradas[i]} | Tel: {telefones[i]} | NIF: {nifs[i]} | Valor: {compras[i]} | Divida:{divfin[i]}"
                    )
                    encontrou = True
            if not encontrou:
                if procurarNome.isdigit():
                    procurarNum = int(procurarNome)
                    for i in range(len(ids)):
                        if ids[i] == procurarNum:
                            print(
                                f"\nPosição {i} | ID {ids[i]} | Nome: {nomes[i]} | Morada: {moradas[i]} | Tel: {telefones[i]} | NIF: {nifs[i]} | Valor: {compras[i]} | Divida:{divfin[i]}"
                            )
                            encontrou = True
            if not encontrou:
                print("\nEsses dados não existem.")
            else:
                posicaoEliminar = int(input("Valide com aescolha da posição: "))
                ids.pop(posicaoEliminar)
                nomes.pop(posicaoEliminar)
                moradas.pop(posicaoEliminar)
                telefones.pop(posicaoEliminar)
                nifs.pop(posicaoEliminar)
                compras.pop(posicaoEliminar)
                divfin.pop(posicaoEliminar)
                print("\nCliente removido com sucesso.")

        case "3":
            print("Pesquisar cliente")
            procurarNome = input("\nEscreva o nome ou ID a pesquisar: ").strip()

            encontrou = False
            for i in range(len(ids)):
                if nomes[i] == procurarNome:
                    print(
                        f"\nPosição {i} | ID {ids[i]} | Nome: {nomes[i]} | Morada: {moradas[i]} | Tel: {telefones[i]} | NIF: {nifs[i]} | Valor: {compras[i]} | Divida:{divfin[i]}"
                    )
                    encontrou = True
            if not encontrou:
                if procurarNome.isdigit():
                    procurarNum = int(procurarNome)
                    for i in range(len(ids)):
                        if ids[i] == procurarNum:
                            print(
                                f"\nPosição {i} | ID {ids[i]} | Nome: {nomes[i]} | Morada: {moradas[i]} | Tel: {telefones[i]} | NIF: {nifs[i]} | Valor: {compras[i]} | Divida:{divfin[i]}"
                            )
                            encontrou = True

            if not encontrou:
                print("\nEsses dados não existem.")

        case "4":
            print("editar cliente")
            procurarNome = input("\nEscreva o nome ou ID a editar: ").strip()

            encontrou = False
            for i in range(len(ids)):
                if nomes[i] == procurarNome:
                    print(
                        f"\nPosição {i} | ID {ids[i]} | Nome: {nomes[i]} | Morada: {moradas[i]} | Tel: {telefones[i]} | NIF: {nifs[i]} | Valor: {compras[i]} | Divida:{divfin[i]}"
                    )
                    encontrou = True
            if not encontrou:
                if procurarNome.isdigit():
                    procurarNum = int(procurarNome)
                    for i in range(len(ids)):
                        if ids[i] == procurarNum:
                            print(
                                f"\nPosição {i} | ID {ids[i]} | Nome: {nomes[i]} | Morada: {moradas[i]} | Tel: {telefones[i]} | NIF: {nifs[i]} | Valor: {compras[i]} | Divida:{divfin[i]}"
                            )
                            encontrou = True

            if not encontrou:
                print("\nEsses dados não existem.")
            else:
                posicaoEditar = int(input("Valide com aescolha da posição: "))
                nomes[posicaoEditar] = input("Nome: ")
                moradas[posicaoEditar] = input("Morada: ")
                while True:
                    novoTelefone = input("Telefone: ").strip()
                    if len(novoTelefone) == 9 and novoTelefone.isdigit():
                        telefones[posicaoEditar] = novoTelefone
                        break
                    else:
                        print(
                            "\nTelefone inválido! Tem de conter exatamente 9 dígitos."
                        )
                # telefones[posicaoEditar] = input("Telefone: ")
                while True:
                    novoNif = input("NIF: ").strip()
                    if len(novoNif) == 9 and novoNif.isdigit():
                        nifs[posicaoEditar] = novoNif
                        break
                    else:
                        print("NIF inválido! Tem de conter exatamente 9 dígitos.")
                # nifs[posicaoEditar] = input("NIF: ")
                valorcompras = float(input("valor da compra: "))
                compras[posicaoEditar] = valorcompras
                if 100 <= valorcompras <= 200:
                    desconto = 5
                elif 200 < valorcompras < 500:
                    desconto = 10
                elif valorcompras >= 500:
                    desconto = 15
                else:
                    desconto = 0
                divfin[posicaoEditar] = valorcompras - (valorcompras * (desconto / 100))

                print("\nCliente Editado com sucesso!!!")

        case "5":
            print("listar clientes")
            for i in range(len(nomes)):
                print(
                    f"\nPosição {i} | ID {ids[i]} | Nome: {nomes[i]} | Morada: {moradas[i]} | Tel: {telefones[i]} | NIF: {nifs[i]} | Valor: {compras[i]} | Divida: {divfin[i]}"
                )
                input("\nPressione Enter para continuar a lista...")

        case _:
            print("\nopção errada, escolha entre 1 e 6")
