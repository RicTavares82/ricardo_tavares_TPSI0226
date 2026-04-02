# Teste Final: Elabore uma base de dados de clientes de uma fábrica de materiais. O programa deverá possibilitar inserção e listagem dos clientes bem como as compras por eles efetuadas( Númcli(Automático), NomCli, morada, tel, nif, compra, Divfin ). Divida final=compra – desconto, valor do desconto se compra for entre 100 e 200 é 5%, se for superior a 200 e inferior a 500 é 10% se superior a 500 é 15%. O programa deve validar todas as entradas e na listagem deve parar cliente a cliente e ser possível busca direta por número de cliente.


# for i in range(20):
#     baseDados = {
#         "Númcli": "???",
#         "NomCli": "",
#         "morada": "",
#         "tel": "",
#         "nif": "",
#         "caompra": "",
#         "Divfin": {compra - desconto},
#     }

# print(baseDados["Númcli"])

while True:
    print("   ------MENU------")
    print("1 - Inserir novo cliente")
    print("2 - remover cliente")
    print("3 - pesquisar cliente")
    print("4 - editar cliente")
    while True:
        num = input("\nEscolha uma opção: ")
        if num > "0" and num < "7":
            break
        else:
            print("\nEscreva um numero válido entre 1 e 6: ")

    match num:
        case "1":
            print("Inserir novo cliente")

            ids = []  # Númcli (Automático)
            nomes = []  # NomCli
            moradas = []  # Morada
            telefones = []  # Tel
            nifs = []  # NIF
            compras = []  # Valor da compra
            divfin = []  # Divfin (Valor com desconto)

            while True:
                novo_id = len(ids) + 1
                ids.append(novo_id)

                novoNome = input("Nome: ")
                nomes.append(novoNome)
                novaMorada = input("Morada: ")
                moradas.append(novaMorada)

                novoTelefone = input("Telefone: ")
                if len(novoTelefone) != 9 and novoTelefone != novoTelefone.isdigit():
                    print("")
                    print("Telefone inválido, deve conter 9 dígitos. Tente novamente.")
                    novoTelefone = input("Telefone: ")
                telefones.append(novoTelefone)

                novoNif = input("NIF: ")
                if len(novoNif) != 9 and novoNif != novoNif.isdigit:
                    print("\nNIF inválido, deve conter 9 numeros. Tente novamente.")
                    novoNif = input("NIF: ")
                nifs.append(novoNif)

                novaCompra = float(input("Valor da compra: (se necessário use o ponto, não a virgula)"))
                if novaCompra != type.novaCompra:

                        
                compras.append(novaCompra)
                if 100 <= novaCompra <= 200:
                    desconto = 0.05
                elif 200 < novaCompra < 500:
                    desconto = 0.10
                elif novaCompra >= 500:
                    desconto = 0.15
                else:
                    desconto = 0
                valor_final = novaCompra * (1 - desconto)
                divfin.append(valor_final)

                print("\nCliente inserido com sucesso!!!\n")
                perguntaSair = input("\nQuer inserir mais clientes? s/n: ")
                if perguntaSair == "n":
                    break

        case "2":
            print("remover cliente")

        case "3":
            print("pesquisar cliente")

        case "4":
            print("editar cliente")

        case "5":
            print("")

        case "6":
            print("")

        case _:
            print("opção errada, escolha entre 1 e 6")

    # function()

    ids = []  # Númcli (Automático)
    nomes = []  # NomCli
    moradas = []  # Morada
    telefones = []  # Tel
    nifs = []  # NIF
    compras = []  # Valor da compra
    divfin = []  # Divfin (Valor com desconto)

    novo_id = len(ids) + 1
    ids.append(novo_id)

    compra = 0
    if 100 <= compra <= 200:
        desconto = 0.05
    elif 200 < compra < 500:
        desconto = 0.10
    elif compra >= 500:
        desconto = 0.15
    else:
        desconto = 0

    # valor_final = compra * (1 - desconto)
    # dividas.append(valor_final)
