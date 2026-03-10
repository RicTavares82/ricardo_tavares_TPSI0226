# Exercício 3

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

if num1 > num2:
    print(f"Decrescente: {num1}, {num2}")
    print(f"Crescente: {num2}, {num1}")
elif num1 < num2:
    print(f"Crescente: {num1}, {num2}")
    print(f"Decrescente: {num2}, {num1}")
else:
    print("Os números são iguais")
