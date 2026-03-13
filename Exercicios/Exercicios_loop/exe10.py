# Exercício 10: Elabore um programa que lê um número e escreve quantos divisores ele possui.
cont = 0
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
