# Exercício 13: Elabore um programa que leia um número e mostre a tabuada. (multiplicar de 1 a 10)
som = 0
con = True
while con:
    numChoice = int(input("Escreva um numero para a tabuada: "))
    for i in range(10):
        som = numChoice * (i + 1)
        print(f"{numChoice} X {i+1} = {som}")

    con = input("Quer inserir outro numero. s/n: ").lower()
    if con == "n":
        con = False
