# Exercício 1: Crie um algoritmo que mostre os 30 primeiros números ímpares e pares.

num = 1
for i in range(30):
    if (num % 2) == 0:
        print(f"o numero {num} é par")

    else:
        print(f"o numero {num} é impar")

    num = num + 1
