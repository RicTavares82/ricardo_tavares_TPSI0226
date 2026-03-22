# Exercício 1

dia = input("Escreva o dia da semana: ")

if dia == "domingo" or dia == "sabado":
    print("Hoje é fim-de-semana")
elif dia == "segunda":
    print("Hoje é dia útil")
elif dia == "terça":
    print("Hoje é dia útil")
elif dia == "quarta":
    print("Hoje é dia útil")
elif dia == "quinta":
    print("Hoje é dia útil")
elif dia == "sexta":
    print("Hoje é dia útil, véspera de fim-de-semana.")
else:
    print("Esse dia não existe!")

print()
# ---------------
# outra forma de mostrar o resultado

match dia:
    case "domingo":
        print("Hoje é fim-de-semana")
    case "sabado":
        print("Hoje é fim-de-semana")
    case "segunda":
        print("Hoje é dia útil")
    case "terça":
        print("Hoje é dia útil")
    case "quarta":
        print("Hoje é dia útil")
    case "quinta":
        print("Hoje é dia útil")
    case "sexta":
        print("Hoje é dia útil, véspera de fim-de-semana.")
    case _:
        print("Esse dia não existe!")
