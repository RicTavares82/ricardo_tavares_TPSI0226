# Exercício 9: Escreva um programa que solicite um número ao utilizador até que o valor deste esteja entre os valores 1 e 100. (Use o ciclo do ... while)


num = int(input("Escreva um numero: "))
while True:
    if num >= 1 and num <= 100:
        print("O numero esta entre 1 e 100")
        break
    else:
        print("O numero nao esta entre 1 e 100, tente novamente")
        num = int(input("Escreva um numero: "))
