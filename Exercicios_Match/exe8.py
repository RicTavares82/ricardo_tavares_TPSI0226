# Exercicio 8

num1 = int(input("Escreva um numero: "))
num2 = int(input("Escreva outro numero: "))

print("Escolha o tipo de operação de calculo.")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
opc = input("Selecione o numero: ")

# soma=input("1 - Soma ")
# sub=input("2 - ")

match opc:
    case "1":
        print(f"{num1 + num2}")
    case "2":
        print(f"{num1 - num2}")
    case "3":
        print(f"{num1 * num2}")
    case "4":
        print(f"{num1 / num2}")
