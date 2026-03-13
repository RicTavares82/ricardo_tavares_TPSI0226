# Exercícios 15: Elabore um programa que escreva no ecrã todas as linhas de código ASCII(0 a 255) e o código correspondente. Dispor de 20 em 20 com a condição de continuação ou saída do programa.

con = True
while con:

    numChoice = int(input("Escreva um numero: "))
    for i in range(numChoice, 0, -1):
        if (numChoice % i) == 0:
            cont += 1
    print(f"O numero {numChoice} é divisivel por {cont} vezes.")
    cont = 0
    con = input("Quer inserir outro numero. s/n: ").lower()

    if con == "n":
        con = False
