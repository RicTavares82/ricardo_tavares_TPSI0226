# Exercício 4: Crie um algoritmo que leia um número inteiro, e diga se ele é um número primo ou não.

readNum = int(input("Escolhe um numero inteiro: "))
count = 0
for i in range(readNum, 0, -1):

    if (readNum % i) == 0:
        count = count + 1
if count == 2:
    print(readNum, " é numero primo.")
else:
    print(f"{readNum} não é primo (tem {count} divisores).")
