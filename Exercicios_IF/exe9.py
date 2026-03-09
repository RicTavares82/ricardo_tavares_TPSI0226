# Exercicio 9

while True:
    escolha = input("Escolha um numero inteiro entre 1 e 12:")
    match escolha:
        case "1":
            print("1 é janeiro.")
        case "2":
            print("2 é fevereiro.")
        case "3":
            print("3 é março.")
        case "4":
            print("4 é abril.")
        case "5":
            print("5 é maio.")
        case "6":
            print("6 é junho.")
        case "7":
            print("7 é julho.")
        case "8":
            print("8 é agosto.")
        case "9":
            print("9 é setembro.")
        case "10":
            print("10 é outubro.")
        case "11":
            print("11 é novembro.")
        case "12":
            print("12 é dezembro.")
        case _:
            print("Número inválido, escolha um número entre 1 e 12.")
