# Exercício 6: Crie um algoritmo que mostre os 10 primeiros números primos.

contaPri = 0  # Contador de quantos números primos encontrámos
i = 2

while contaPri < 10:
    divisores = 0

    # Testamos todos os números de 1 até i para ver se são divisores
    for j in range(1, i + 1):
        if i % j == 0:
            divisores += 1

    # Se encontrou exatamente 2 divisores, é primo
    if divisores == 2:
        print(f"{i} é primo.", end=" | ")
        contaPri += 1

    i += 1
